import Jetson.GPIO as GPIO
import time
import tkinter as tk
import cv2
import numpy as np
import os
import threading
import queue
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms

# PWMおよびモーター制御ピンの設定
SERVO_PIN = 32  # サーボモーターPWMピン
DC_PIN = 33     # DCモーターPWMピン
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

# モデルのロード
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load("model.pth", map_location=device)  # 学習済みモデル
model.eval()

# 画像変換の設定
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((60, 60)),
    transforms.ToTensor(),
])

# キャプチャしたデータを保存するディレクトリ
base_dir = 'captured_data'
os.makedirs(base_dir, exist_ok=True)

# 最近保存したファイルパスを保存するリスト
recent_files = []

# カメラの設定
cap = cv2.VideoCapture(0)  # カメラ0を使用
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FPS, 30)

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
    GPIO.output(IN1_PIN, GPIO.HIGH)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.HIGH)
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(current_speed)

# DCモーター後退設定
def move_backward():
    print(f"後退中 | 速度: {current_speed}, 角度: {current_angle}")
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.HIGH)
    GPIO.output(IN3_PIN, GPIO.LOW)
    GPIO.output(IN4_PIN, GPIO.HIGH)
    pwm_dc.ChangeDutyCycle(current_speed)

# DCモーター停止関数
def stop_motors():
    print("モーター停止")
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.LOW)
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(0)

# 画像処理関数
def process_image(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 25, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    
    lower_yellow = np.array([10, 30, 30])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)
    result = cv2.bitwise_and(image, image, mask=combined_mask)

    return result

# 画像を学習用モデルに入力するために前処理を行う
def classify_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return predicted.item()

# モーターの動作
def control_motors(angle):
    if angle == 0:  # 左折
        set_servo_angle(DEFAULT_ANGLE - ANGLE_STEP)
    elif angle == 1:  # 少し左折
        set_servo_angle(DEFAULT_ANGLE - ANGLE_STEP // 2)
    elif angle == 2:  # 正面
        set_servo_angle(DEFAULT_ANGLE)
    elif angle == 3:  # 少し右折
        set_servo_angle(DEFAULT_ANGLE + ANGLE_STEP // 2)
    elif angle == 4:  # 右折
        set_servo_angle(DEFAULT_ANGLE + ANGLE_STEP)

# 画像保存用スレッド
def capture_and_save_image_task():
    while True:
        ret, frame = cap.read()
        if ret:
            processed_image = process_image(frame)
            predicted_angle = classify_image(processed_image)
            control_motors(predicted_angle)
            print(f"予測結果: {predicted_angle} (0:左折, 4:右折)")

            # 画像保存
            h, w = frame.shape[:2]
            y1 = h // 3
            y2 = h
            roi = frame[y1:y2, :]
            resized = cv2.resize(roi, (60, 60))

            speed_dir = os.path.join(base_dir, f"speed_{current_speed}")
            angle_dir = os.path.join(speed_dir, f"angle_{current_angle}")
            os.makedirs(angle_dir, exist_ok=True)

            filename = os.path.join(angle_dir, f"{time.time():.0f}.jpg")
            cv2.imwrite(filename, processed_image)
            print(f"画像を保存しました: {filename}")

        time.sleep(0.1)

# 画像保存スレッドの開始
image_thread = threading.Thread(target=capture_and_save_image_task)
image_thread.start()

# イベント処理
def on_key_press(event):
    if event.keysym == 'Escape':
        root.quit()

root = tk.Tk()
root.bind("<KeyPress>", on_key_press)
root.mainloop()
