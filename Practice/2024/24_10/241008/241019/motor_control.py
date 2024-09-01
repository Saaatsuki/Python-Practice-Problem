# import Jetson.GPIO as GPIO
# from pynput import keyboard

# # GPIOピンの設定
# RIGHT_MOTOR_PIN = 17  # 右回転用ピン
# LEFT_MOTOR_PIN = 27   # 左回転用ピン

# # GPIOの初期化
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(RIGHT_MOTOR_PIN, GPIO.OUT)
# GPIO.setup(LEFT_MOTOR_PIN, GPIO.OUT)

# # モーターを右回転させる関数
# def turn_right():
#     print("右回転")
#     GPIO.output(RIGHT_MOTOR_PIN, GPIO.HIGH)  # 右モーターON
#     GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)    # 左モーターOFF

# # モーターを左回転させる関数
# def turn_left():
#     print("左回転")
#     GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)   # 右モーターOFF
#     GPIO.output(LEFT_MOTOR_PIN, GPIO.HIGH)   # 左モーターON

# # モーターを停止させる関数
# def stop():
#     print("停止")
#     GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)   # 右モーターOFF
#     GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)     # 左モーターOFF

# # キーボードのキーが押されたときの処理
# def on_press(key):
#     try:
#         if key == keyboard.Key.left:  # 左矢印キー
#             turn_left()
#         elif key == keyboard.Key.right:  # 右矢印キー
#             turn_right()
#     except AttributeError:
#         pass

# # キーボードのリスナーを開始
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

# # プログラム終了時のクリーンアップ
# GPIO.cleanup()
