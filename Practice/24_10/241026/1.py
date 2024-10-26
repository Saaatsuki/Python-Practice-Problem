import Jetson.GPIO as GPIO  # Jetson NanoのGPIO制御ライブラリをインポート
import time                 # 待機処理を行うためのtimeライブラリをインポート
import tkinter as tk        # GUIを作成するためのtkinterライブラリをインポート

# PWMおよびモーター制御ピンの設定
SERVO_PIN = 32  # サーボモーターのPWM制御用ピン番号
DC_PIN = 33     # DCモーターのPWM制御用ピン番号

# GPIOピンの設定（Jetson Nanoのボード番号に基づく）
IN1_PIN = 13  # モーター1の方向制御用ピン（IN1）
IN2_PIN = 15  # モーター1の方向制御用ピン（IN2）
IN3_PIN = 16  # モーター2の方向制御用ピン（IN3）
IN4_PIN = 18  # モーター2の方向制御用ピン（IN4）

# GPIO設定（警告無効化、ピン番号の設定）
GPIO.setwarnings(False)      # GPIO警告を無効化
GPIO.setmode(GPIO.BOARD)     # ボード番号のピン配置で設定
GPIO.setup(SERVO_PIN, GPIO.OUT)  # サーボモーターピンを出力モードに設定
GPIO.setup(DC_PIN, GPIO.OUT)     # DCモーターピンを出力モードに設定
GPIO.setup(IN1_PIN, GPIO.OUT)    # IN1ピンを出力モードに設定
GPIO.setup(IN2_PIN, GPIO.OUT)    # IN2ピンを出力モードに設定
GPIO.setup(IN3_PIN, GPIO.OUT)    # IN3ピンを出力モードに設定
GPIO.setup(IN4_PIN, GPIO.OUT)    # IN4ピンを出力モードに設定

# サーボモーターの初期設定（50Hz、PWM開始）
pwm_servo = GPIO.PWM(SERVO_PIN, 50)  # サーボ用PWM信号（50Hz）
pwm_servo.start(7.5)                 # 初期位置（中立角度）を設定

# DCモーターのPWM設定（速度制御用に100Hz）
pwm_dc = GPIO.PWM(DC_PIN, 100)  # DCモーター用PWM信号（100Hz）
pwm_dc.start(0)                 # 初期速度を0%に設定

# 現在の速度設定用変数
current_speed = 75  # 初期速度を75%に設定
speed_step = 5      # 速度の増減単位（5%）

# サーボモーターの角度を調整する関数
def set_servo_angle(angle):
    # 角度に基づき対応するデューティサイクルを計算
    duty = 3.0 + (angle / 180.0) * 9.5
    pwm_servo.ChangeDutyCycle(duty)  # 計算されたデューティサイクルをサーボモーターに適用
    time.sleep(0.5)                  # サーボモーターが動くまで待機

# DCモーターの前進動作を設定する関数
def move_forward():
    print("Moving forward with speed:", current_speed)  # 前進情報を出力
    GPIO.output(IN1_PIN, GPIO.HIGH)  # モーター1を前進方向に設定
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.HIGH)  # モーター2を前進方向に設定
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(current_speed)  # 設定された速度を適用

# DCモーターの後退動作を設定する関数
def move_backward():
    print("Moving backward with speed:", current_speed)  # 後退情報を出力
    GPIO.output(IN1_PIN, GPIO.LOW)   # モーター1を後退方向に設定
    GPIO.output(IN2_PIN, GPIO.HIGH)
    GPIO.output(IN3_PIN, GPIO.LOW)   # モーター2を後退方向に設定
    GPIO.output(IN4_PIN, GPIO.HIGH)
    pwm_dc.ChangeDutyCycle(current_speed)  # 設定された速度を適用

# DCモーターを停止する関数
def stop_motors():
    print("Stopping motors")  # 停止情報を出力
    GPIO.output(IN1_PIN, GPIO.LOW)  # モーター1を停止
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.LOW)  # モーター2を停止
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(0)       # モーター速度を0に設定（完全停止）

# 速度を増加させる関数（Fキー押下）
def increase_speed():
    global current_speed
    if current_speed + speed_step <= 100:  # 速度が100%を超えない場合のみ増加
        current_speed += speed_step
        print("Increased speed to:", current_speed)  # 新しい速度を出力
    else:
        print("Max speed reached")  # 速度が最大の場合のメッセージ

# 速度を減少させる関数（Gキー押下）
def decrease_speed():
    global current_speed
    if current_speed - speed_step >= 0:  # 速度が0%以上の場合のみ減少
        current_speed -= speed_step
        print("Decreased speed to:", current_speed)  # 新しい速度を出力
    else:
        print("Min speed reached")  # 速度が最小の場合のメッセージ

# キーの状態管理辞書（A, D, W, S, F, Gキー）
key_pressed = {
    'a': False,
    'd': False,
    'w': False,
    's': False
}

# キーが押されたときのイベント処理関数
def on_key_press(event):
    if event.keysym == 'a':
        key_pressed['a'] = True
    elif event.keysym == 'd':
        key_pressed['d'] = True
    elif event.keysym == 'w':
        key_pressed['w'] = True
        move_forward()  # Wキーで前進
    elif event.keysym == 's':
        key_pressed['s'] = True
        move_backward()  # Sキーで後退
    elif event.keysym == 'f':
        increase_speed()  # Fキーで速度増加
    elif event.keysym == 'g':
        decrease_speed()  # Gキーで速度減少
    elif event.keysym == "Escape":
        root.quit()  # Escキーでプログラム終了

# キーが離されたときのイベント処理関数
def on_key_release(event):
    if event.keysym == 'a':
        key_pressed['a'] = False
    elif event.keysym == 'd':
        key_pressed['d'] = False
    elif event.keysym == 'w':
        key_pressed['w'] = False
        stop_motors()  # Wキーを離したらモーター停止
    elif event.keysym == 's':
        key_pressed['s'] = False
        stop_motors()  # Sキーを離したらモーター停止

# サーボモーターを中立位置に戻す関数
def reset_servo_to_neutral():
    if not key_pressed['a'] and not key_pressed['d']:
        set_servo_angle(100)  # サーボモーターを100度（中立）に設定

# キーの状態をチェックして動作を制御
def check_keys():
    if key_pressed['a']:
        set_servo_angle(60)  # Aキーで左回転
    if key_pressed['d']:
        set_servo_angle(140)  # Dキーで右回転

    # どのキーも押されていない場合、サーボモーターを中立に設定
    reset_servo_to_neutral()

    # 100msごとにキーの状態をチェック
    root.after(100, check_keys)

# tkinter GUI設定とキーイベントのバインド
root = tk.Tk()

# キーボードの押下・解放イベントをバインド
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

# キーの状態チェック
check_keys()

# Tkinterメインループ（GUIのイベントループを開始）
root.mainloop()

# プログラム終了時のGPIOのクリーンアップ
pwm_servo.stop()   # サーボPWMを停止
pwm_dc.stop()      # DCモータPWMを停止
GPIO.cleanup()     # GPIO設定をリセット
