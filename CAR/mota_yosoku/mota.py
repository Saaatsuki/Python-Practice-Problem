import threading
import time
import Jetson.GPIO as GPIO

# GPIOの設定
GPIO.setmode(GPIO.BCM)

# モーター用GPIO設定
motor_pins = {
    "left_forward": 23,
    "left_backward": 24,
    "right_forward": 27,
    "right_backward": 22
}
for pin in motor_pins.values():
    GPIO.setup(pin, GPIO.OUT)

# モーター制御関数
def move_motor(left_speed, right_speed):
    GPIO.output(motor_pins["left_forward"], GPIO.HIGH if left_speed > 0 else GPIO.LOW)
    GPIO.output(motor_pins["left_backward"], GPIO.HIGH if left_speed < 0 else GPIO.LOW)
    GPIO.output(motor_pins["right_forward"], GPIO.HIGH if right_speed > 0 else GPIO.LOW)
    GPIO.output(motor_pins["right_backward"], GPIO.HIGH if right_speed < 0 else GPIO.LOW)

# サーボモーター設定
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50HzのPWM
servo.start(7.5)  # 初期角度（90度）

def set_servo_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)  # 0度から180度に対応
    servo.ChangeDutyCycle(duty_cycle)

# 角度情報を保持する共有変数
current_direction = 2  # 初期値を直進に設定

def update_direction():
    global current_direction
    while True:
        try:
            with open("direction_data.txt", "r") as file:
                data = file.read().strip()
                if data.isdigit():
                    current_direction = int(data)
        except FileNotFoundError:
            pass
        time.sleep(0.1)  # 100ms間隔で確認

def control_motor():
    while True:
        if current_direction == 0:  # 左折
            set_servo_angle(52)
            move_motor(0.5, 1)
        elif current_direction == 1:  # 少し左折
            set_servo_angle(77)
            move_motor(1, 1)
        elif current_direction == 2:  # 直進
            set_servo_angle(102)
            move_motor(1, 1)
        elif current_direction == 3:  # 少し右折
            set_servo_angle(127)
            move_motor(1, 1)
        elif current_direction == 4:  # 右折
            set_servo_angle(152)
            move_motor(1, 0.5)
        time.sleep(0.1)  # 100ms間隔で更新

# スレッド作成
direction_thread = threading.Thread(target=update_direction, daemon=True)
motor_thread = threading.Thread(target=control_motor, daemon=True)

# スレッド開始
direction_thread.start()
motor_thread.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("終了します...")

finally:
    servo.stop()
    GPIO.cleanup()
