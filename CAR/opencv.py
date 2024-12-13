# サーボモーターとDCモーターのテストコード
# 必要なライブラリをインポート
# https://bootstrap.pypa.io/get-pip.py

import Jetson.GPIO as GPIO
import time
import tkinter as tk
import cv2
import numpy as np
import os
import threading
import queue

# PWMおよびモーター制御ピンの設定
SERVO_PIN = 32  # サーボモーターPWMピン
DC_PIN = 33     # DCモーターPWMピン

# GPIOピンの設定（Jetson NanoのGPIO番号）
IN1_PIN = 13  # モーター1、IN1
IN2_PIN = 15  # モーター1、IN2
IN3_PIN = 16  # モーター2、IN3
IN4_PIN = 18  # モーター2、IN4

DEFAULT_ANGLE = 102  # 中立角度
DEFAULT_SPEED = 30   # 初期速度
ANGLE_STEP = 25      # 角度の増減幅
SPEED_STEP = 1       # 速度の増減幅

# GPIOの設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)
GPIO.setup(IN3_PIN, GPIO.OUT)
GPIO.setup(IN4_PIN, GPIO.OUT)

# サーボモーター用PWM 50Hzの初期化
pwm_servo = GPIO.PWM(SERVO_PIN, 50)
pwm_servo.start(7.5)  # 中立角度 (100度に対応)

# DCモーター用PWM 100Hzの初期化（速度制御用）
pwm_dc = GPIO.PWM(DC_PIN, 100)
pwm_dc.start(0)  # 初期速度0%

# 現在の速度を保存する変数
current_speed = DEFAULT_SPEED

# 現在の角度を保存する変数
current_angle = DEFAULT_ANGLE

# キャプチャしたデータを保存するディレクトリ
base_dir = 'captured_data'
os.makedirs(base_dir, exist_ok=True)

# 最近保存したファイルパスを保存するリスト
recent_files = []

# カメラの設定
cap = cv2.VideoCapture(0)  # カメラ0を使用
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # バッファサイズを1に設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 解像度の幅を設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 解像度の高さを設定
cap.set(cv2.CAP_PROP_FPS, 30)  # FPSを設定

# タスクキューを作成
task_queue = queue.Queue()

# サーボモーターの角度調整関数
def set_servo_angle(angle):
    if angle > DEFAULT_ANGLE + ANGLE_STEP * 2:
        print("最大角度を超えました")
        return
    if angle < DEFAULT_ANGLE - ANGLE_STEP * 2:
        print("最小角度を超えました")
        return
    global current_angle
    print(f"角度を調整中: {angle}")
    duty = 3.0 + (angle / 180.0) * 9.5  # 角度に対応するデューティ比を計算
    pwm_servo.ChangeDutyCycle(duty)
    current_angle = angle
    time.sleep(0.1)  # サーボモーターが動作する時間を確保

# DCモーター前進設定
def move_forward():
    print(f"前進中 | 速度: {current_speed}, 角度: {current_angle}")
    GPIO.output(IN1_PIN, GPIO.HIGH)  # モーター1前進
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.HIGH)  # モーター2前進
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度を調整

# DCモーター後退設定
def move_backward():
    print(f"後退中 | 速度: {current_speed}, 角度: {current_angle}")
    GPIO.output(IN1_PIN, GPIO.LOW)  # モーター1後退
    GPIO.output(IN2_PIN, GPIO.HIGH)
    GPIO.output(IN3_PIN, GPIO.LOW)  # モーター2後退
    GPIO.output(IN4_PIN, GPIO.HIGH)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度を調整

# DCモーター停止関数
def stop_motors():
    print("モーター停止")
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.LOW)
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(0)  # 速度を0に設定（停止）

# 白線・黄色線の検出フィルタ関数
def filter_white_yellow(image):
    # 画像をHSV色空間に変換
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 白色の範囲を設定
    lower_white = np.array([0, 0, 200])  # 下限値 (H, S, V)
    upper_white = np.array([180, 25, 255])  # 上限値
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # 黄色の範囲を設定
    lower_yellow = np.array([10, 30, 30])  # 下限値
    upper_yellow = np.array([40, 255, 255])  # 上限値
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 白色と黄色を結合したマスク
    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)

    # 元の画像で白色と黄色を強調
    result = cv2.bitwise_and(image, image, mask=combined_mask)

    return result

# 画像保存用スレッド
def capture_and_save_image_task():
    while True:
        try:
            # キューからタスクを取得
            task = task_queue.get()
            if task is None:  # Noneなら終了
                break

            speed, angle, count = task

            cap.grab()
            ret, frame = cap.read()
            if ret:
                # 画像をROI（注目領域）に変換
                h, w = frame.shape[:2]
                y1 = h // 3  # 高さの1/3地点
                y2 = h
                roi = frame[y1:y2, :]

                # 60 x 60 サイズにリサイズ
                resized = cv2.resize(roi, (60, 60))

                # 白線・黄色線のフィルタ処理
                mask = filter_white_yellow(resized)

                # 保存ディレクトリの構成
                speed_dir = os.path.join(base_dir, f"speed_{speed}")
                angle_dir = os.path.join(speed_dir, f"angle_{angle}")
                os.makedirs(angle_dir, exist_ok=True)

                # 画像の保存
                filename = os.path.join(angle_dir, f"{count:04d}.jpg")
                cv2.imwrite(filename, mask)
                print(f"画像を保存しました: {filename}")

                # 最近のファイルを更新
                recent_files.append(filename)
                if len(recent_files) > 10:
                    recent_files.pop(0)  # 最新10件のみ保存

        except Exception as e:
            print(f"画像保存エラー: {e}")

# 最近保存したファイルを削除
def delete_recent_files():
    global recent_files
    if recent_files:
        print("最近の10件のファイルを削除中...")
        for file_path in reversed(recent_files):
            try:
                os.remove(file_path)
                print(f"削除しました: {file_path}")
            except FileNotFoundError:
                print(f"ファイルが見つかりません: {file_path}")
        recent_files.clear()
    else:
        print("削除するファイルがありません")

# 画像保存スレッドの開始
image_thread = threading.Thread(target=capture_and_save_image_task)
image_thread.start()

# ---以下、イベント処理やGUIの処理

# キャプチャのリクエスト関数
capture_count = 0
def request_capture():
    global capture_count
    
    # 作業キューにリクエストを追加
    task_queue.put((current_speed, current_angle, capture_count))
    capture_count += 1

# 速度を増加させる関数（Fキー）
def increase_speed():
    global current_speed
    if current_speed + SPEED_STEP <= 100:
        current_speed += SPEED_STEP
        print("速度を増加しました:", current_speed)
        # 現在前進または後退中の場合、速度を更新
        if key_pressed['w'] or key_pressed['s']:
            pwm_dc.ChangeDutyCycle(current_speed)
    else:
        print("最大速度に達しました")

# 速度を減少させる関数（Gキー）
def decrease_speed():
    global current_speed
    if current_speed - SPEED_STEP >= SPEED_STEP:
        current_speed -= SPEED_STEP
        print("速度を減少しました:", current_speed)
        # 現在前進または後退中の場合、速度を更新
        if key_pressed['w'] or key_pressed['s']:
            pwm_dc.ChangeDutyCycle(current_speed)
    else:
        print("最小速度に達しました")

# キー状態を管理する辞書（W、Sキー）
key_pressed = {
    'w': False,
    's': False
}

# キーが押されたときの処理
def on_key_press(event):
    if event.keysym == 'a':
        set_servo_angle(current_angle - ANGLE_STEP)  # 左に角度調整
    elif event.keysym == 'd':
        set_servo_angle(current_angle + ANGLE_STEP)  # 右に角度調整
    if event.keysym == 'w':
        key_pressed['w'] = True  # 前進
    elif event.keysym == 's':
        key_pressed['s'] = True  # 後退
    if event.keysym == 'f':
        increase_speed()  # Fキーで速度増加
    elif event.keysym == 'g':
        decrease_speed()  # Gキーで速度減少
    elif event.keysym == 'BackSpace':
        delete_recent_files()  # BackSpaceで最近のファイルを削除
    if event.keysym == "Escape":
        root.quit()  # Escapeキーで終了

# キーが離されたときの処理
def on_key_release(event):
    if event.keysym == 'w':
        key_pressed['w'] = False  # 前進停止
    if event.keysym == 's':
        key_pressed['s'] = False  # 後退停止

# キー状態を定期的にチェックする関数
def check_keys(): 
    if key_pressed['w']:
        move_forward()  # 前進
        request_capture()  # 画像保存リクエスト
    elif key_pressed['s']:
        move_backward()  # 後退
        request_capture()  # 画像保存リクエスト
    else:
        stop_motors()  # モーター停止

    # 100ms毎にキー状態をチェック
    root.after(100, check_keys)

# Tkinter GUIの設定
root = tk.Tk()

# キーボードイベントのバインディング
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

# キー状態の確認
check_keys()

# Tkinterのメインループ
root.mainloop()

# プログラム終了時のGPIOのクリーンアップ
set_servo_angle(DEFAULT_ANGLE)  # サーボモーターを中立角度に戻す
pwm_dc.stop()  # DCモーターのPWM停止
GPIO.cleanup()  # GPIOのクリーンアップ
cap.release()  # カメラを解放
cv2.destroyAllWindows()  # OpenCVウィンドウを破棄

# スレッド終了信号を送信
task_queue.put(None)
image_thread.join()