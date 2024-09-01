import Jetson.GPIO as GPIO
import time
import tkinter as tk

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
pwm_servo.start(7.5)  # 初期中立角度（100度）

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

# キーの状態を管理（W、Sキー）
key_pressed = {
    'w': False,
    's': False
}

# キー押下時の処理
def on_key_press(event):
    if event.keysym == 'a':
        set_servo_angle(current_angle - angle_step)
    elif event.keysym == 'd':
        set_servo_angle(current_angle + angle_step)
    if event.keysym == 'w':
        key_pressed['w'] = True
    elif event.keysym == 's':
        key_pressed['s'] = True
    if event.keysym == "Escape":
        root.quit()

# キー離した時の処理
def on_key_release(event):
    if event.keysym == 'w':
        key_pressed['w'] = False
    if event.keysym == 's':
        key_pressed['s'] = False

# キー状態を確認するループ
def check_keys():
    if key_pressed['w']:
        move_forward()
    elif key_pressed['s']:
        move_backward()
    else:
        stop_motors()
    # 100msごとにキー状態を確認
    root.after(100, check_keys)

# スライダーを使って速度調整
def update_speed(val):
    global current_speed
    current_speed = int(val)
    pwm_dc.ChangeDutyCycle(current_speed)

# tkinter GUIの設定
root = tk.Tk()

# 速度スライダーの設定
speed_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", label="速度調整", command=update_speed)
speed_slider.set(current_speed)  # 初期値
speed_slider.pack()

# キーボードイベントのバインディング
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

# キー状態の確認開始
check_keys()

# Tkinterのメインループ
root.mainloop()

# プログラム終了時のGPIOクリーンアップ
set_servo_angle(100)
pwm_dc.stop()
GPIO.cleanup()