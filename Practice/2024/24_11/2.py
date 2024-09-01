# PWMおよびモーター制御ピンの設定
SERVO_PIN = 32  # サーボモーターのPWMピン
DC_PIN = 33     # DCモーターのPWMピン

# GPIOピンの設定 (Jetson NanoのGPIOピン番号)
IN1_PIN = 13  # モーター1、IN1
IN2_PIN = 15  # モーター1、IN2
IN3_PIN = 16  # モーター2、IN3
IN4_PIN = 18  # モーター2、IN4

# GPIOの設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)
GPIO.setup(IN3_PIN, GPIO.OUT)
GPIO.setup(IN4_PIN, GPIO.OUT)

# サーボモーター 50HzでPWM初期化
pwm_servo = GPIO.PWM(SERVO_PIN, 50)
pwm_servo.start(7.5)  # 初期の中立角度 (100度)

# DCモーター PWM 100Hzの設定 (速度制御のための周波数)
pwm_dc = GPIO.PWM(DC_PIN, 100)
pwm_dc.start(0)  # 初期速度0%

# 現在の速度の変数
current_speed = 75  # 初期速度 (75%)
speed_step = 5  # 速度の増減単位

# サーボモーターの角度調整関数
def set_servo_angle(angle):
    duty = 3.0 + (angle / 180.0) * 9.5  # 角度に応じたデューティサイクルを計算
    pwm_servo.ChangeDutyCycle(duty)
    time.sleep(0.5)  # サーボモーターが動くまでの時間待機

# DCモーターを前進させる設定 (前進時の方向設定)
def move_forward():
    print("前進中の速度:", current_speed)
    GPIO.output(IN1_PIN, GPIO.HIGH)  # モーター1前進
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.HIGH)  # モーター2前進
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度制御

# DCモーターを後退させる設定 (後退時の方向設定)
def move_backward():
    print("後退中の速度:", current_speed)
    GPIO.output(IN1_PIN, GPIO.LOW)   # モーター1後退
    GPIO.output(IN2_PIN, GPIO.HIGH)
    GPIO.output(IN3_PIN, GPIO.LOW)   # モーター2後退
    GPIO.output(IN4_PIN, GPIO.HIGH)
    pwm_dc.ChangeDutyCycle(current_speed)  # 速度制御

# DCモーターの停止関数 (モーター停止)
def stop_motors():
    print("モーター停止")
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.output(IN3_PIN, GPIO.LOW)
    GPIO.output(IN4_PIN, GPIO.LOW)
    pwm_dc.ChangeDutyCycle(0)  # 速度を0に設定 (停止)

# 速度増加関数 (Fキー)
def increase_speed():
    global current_speed
    if current_speed + speed_step <= 100:
        current_speed += speed_step
        print("速度が増加しました:", current_speed)
    else:
        print("最大速度に達しました")

# 速度減少関数 (Gキー)
def decrease_speed():
    global current_speed
    if current_speed - speed_step >= 0:
        current_speed -= speed_step
        print("速度が減少しました:", current_speed)
    else:
        print("最小速度に達しました")

# キーの状態管理 (A, D, W, S, F, Gキー)
key_pressed = {
    'a': False,
    'd': False,
    'w': False,
    's': False
}

def on_key_press(event):
    if event.keysym == 'a':
        key_pressed['a'] = True
    elif event.keysym == 'd':
        key_pressed['d'] = True
    elif event.keysym == 'w':
        key_pressed['w'] = True
        move_forward()  # Wキーを押した時、即座に前進
    elif event.keysym == 's':
        key_pressed['s'] = True
        move_backward()  # Sキーを押した時、即座に後退
    elif event.keysym == 'f':
        increase_speed()  # Fキーで速度増加
    elif event.keysym == 'g':
        decrease_speed()  # Gキーで速度減少
    elif event.keysym == "Escape":
        root.quit()

def on_key_release(event):
    if event.keysym == 'a':
        key_pressed['a'] = False
    elif event.keysym == 'd':
        key_pressed['d'] = False
    elif event.keysym == 'w':
        key_pressed['w'] = False
        stop_motors()  # Wキーを離した時にモーター停止
    elif event.keysym == 's':
        key_pressed['s'] = False
        stop_motors()  # Sキーを離した時にモーター停止

# サーボモーターを中立に設定
def reset_servo_to_neutral():
    if not key_pressed['a'] and not key_pressed['d']:
        set_servo_angle(100)  # サーボモーターを100度に設定 (中立)

def check_keys():
    if key_pressed['a']:
        set_servo_angle(60)
    if key_pressed['d']:
        set_servo_angle(140)

    # どのキーも押されていない場合、サーボモーターを中立に設定
    reset_servo_to_neutral()

    # 100msごとにキーの状態を確認
    root.after(100, check_keys)

# tkinter GUIの設定
root = tk.Tk()

# キーボードイベントのバインド
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

# キーの状態確認
check_keys()

# Tkinterメインループ
root.mainloop()

# プログラム終了時のGPIOクリーンアップ
pwm_servo.stop()
pwm_dc.stop()
GPIO.cleanup()
