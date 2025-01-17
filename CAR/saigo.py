import Jetson.GPIO as GPIO
import time
import tkinter as tk
import cv2
import numpy as np
import torch
import torch.nn as nn
import threading
import queue
from torchvision import transforms
import socket  # 追加：角度データを受け取るため

# PWMおよびモーター制御ピンの設定
SERVO_PIN = 32  # サーボモーターのPWMピン
DC_PIN = 33     # DCモーターのPWMピン

# GPIOピン設定（Jetson NanoのGPIOピン番号）
IN1_PIN = 13  # モーター1, IN1
IN2_PIN = 15  # モーター1, IN2
IN3_PIN = 16  # モーター2, IN3
IN4_PIN = 18  # モーター2, IN4

# GPIO設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)
GPIO.setup(IN3_PIN, GPIO.OUT)
GPIO.setup(IN4_PIN, GPIO.OUT)

# サーボモーターの50Hz PWM初期化
pwm_servo = GPIO.PWM(SERVO_PIN, 50)
pwm_servo.start(7.5)  # 初期中立角度（90度）

# DCモーターのPWM設定（速度制御用、周波数100Hz）
pwm_dc = GPIO.PWM(DC_PIN, 100)
pwm_dc.start(0)  # 初期速度0%

# 現在の速度を保持する変数
current_speed = 70  # 初期速度（70%）
speed_step = 30     # 速度増減単位

# 現在の角度を保持する変数
current_angle = 100  # 初期角度（100度）
angle_step = 15      # 角度増減単位

# サーボモーターの角度を調整する関数
def set_servo_angle(angle):
    if angle > 130:
        print("最大角度に到達しました")
        return
    if angle < 70:
        print("最小角度に到達しました")
        return
    global current_angle
    print(f"角度を調整中: {angle}")
    duty = 3.0 + (angle / 180.0) * 9.5  # 角度に応じたデューティサイクルを計算
    pwm_servo.ChangeDutyCycle(duty)
    current_angle = angle
    time.sleep(0.1)  # サーボモーターが動作する時間を待機

# DCモーターを前進させる関数
def move_forward():
    print(f"前進中 - 速度: {current_speed}, 角度: {current_angle}")
    GPIO.output(IN1_PIN, GPIO.HIGH)  # モーター1前進
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.HIGH)  # モーター2前進
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度制御

# DCモーターを後退させる関数
def move_backward():
    print(f"後退中 - 速度: {current_speed}, 角度: {current_angle}")
    GPIO.output(IN1_PIN, GPIO.LOW)   # モーター1後退
    GPIO.output(IN2_PIN, GPIO.HIGH)
    GPIO.output(IN3_PIN, GPIO.LOW)   # モーター2後退
    GPIO.output(IN4_PIN, GPIO.HIGH)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度制御

# DCモーターを停止する関数
def stop_motors():
    print("モーターを停止します")
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.LOW)
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(0)  # 速度を0に設定（停止）

# カメラの設定
cap = cv2.VideoCapture(0)  # カメラ0を使用
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # バッファサイズを1に設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 解像度の幅を設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 解像度の高さを設定
cap.set(cv2.CAP_PROP_FPS, 30)  # FPSを設定

# CNNモデルのロード
class DirectionModel(nn.Module):
    def __init__(self):
        super(DirectionModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(128 * 60 * 80, 128)
        self.fc2 = nn.Linear(128, 5)  # 5つのクラス（0～4）

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = x.view(x.size(0), -1)  # Flatten
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# モデルのインスタンス作成
model = DirectionModel()
model.load_state_dict(torch.load("trained_model.pth"))
model.eval()

# 画像前処理
preprocess = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((60, 80)),  # モデルの入力サイズに合わせる
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 画像保存用スレッド
def capture_and_save_image_task():
    while True:
        try:
            ret, frame = cap.read()
            if ret:
                # 白線・黄色線のフィルタ処理
                mask = filter_white_yellow(frame)

                # 画像前処理
                input_image = preprocess(mask).unsqueeze(0)  # バッチ次元を追加

                # モデルの推論
                with torch.no_grad():
                    output = model(input_image)
                    _, predicted = torch.max(output, 1)
                    print(f"予測結果: {predicted.item()}")

                time.sleep(1)  # 画像取得間隔
        except Exception as e:
            print(f"エラー: {e}")
            break

# 画像処理（白線・黄色線をフィルタリング）
def filter_white_yellow(frame):
    lower_white = np.array([0, 0, 200])  # 白色の下限
    upper_white = np.array([180, 30, 255])  # 白色の上限
    lower_yellow = np.array([20, 100, 100])  # 黄色の下限
    upper_yellow = np.array([40, 255, 255])  # 黄色の上限
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # HSV色空間に変換

    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    combined_mask = cv2.bitwise_or(mask_white, mask_yellow)  # 白線と黄色線を合成
    result = cv2.bitwise_and(frame, frame, mask=combined_mask)
    return result

# GUIの設定
root = tk.Tk()
root.title("自律走行車")
root.geometry("400x200")

# GUIボタン設定
button_forward = tk.Button(root, text="前進", command=move_forward)
button_forward.pack(fill=tk.X)

button_backward = tk.Button(root, text="後退", command=move_backward)
button_backward.pack(fill=tk.X)

button_stop = tk.Button(root, text="停止", command=stop_motors)
button_stop.pack(fill=tk.X)

# カメラ制御スレッドの起動
camera_thread = threading.Thread(target=capture_and_save_image_task, daemon=True)
camera_thread.start()

root.mainloop()
