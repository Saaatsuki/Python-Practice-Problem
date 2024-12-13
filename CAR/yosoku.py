import cv2
import numpy as np
import threading
import Jetson.GPIO as GPIO
import torch
from torchvision import transforms
from torch.autograd import Variable
from torch import nn

# GPIOの設定
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50HzのPWM
servo.start(7.5)  # 初期角度（90度）

def set_servo_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)  # 0度から180度に対応
    servo.ChangeDutyCycle(duty_cycle)

# モーター用GPIO
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

# カメラキャプチャ
cap = cv2.VideoCapture(0)

# 白線と黄色線を検出する関数
def filter_white_yellow(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    white_lower = np.array([0, 0, 200])
    white_upper = np.array([180, 30, 255])
    yellow_lower = np.array([15, 100, 100])
    yellow_upper = np.array([35, 255, 255])

    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)
    return cv2.bitwise_and(image, image, mask=combined_mask)

# モデルの読み込み
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(16 * 112 * 112, 5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = x.view(-1, 16 * 112 * 112)
        x = self.fc1(x)
        return x

model = SimpleCNN()
model.load_state_dict(torch.load('trained_model.pth'))
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_direction(frame):
    input_frame = transform(frame).unsqueeze(0)
    input_frame = Variable(input_frame)
    output = model(input_frame)
    _, predicted = torch.max(output.data, 1)
    return predicted.item()

# 予測結果送信用スレッド
def send_predictions():
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        filtered_frame = filter_white_yellow(frame)
        direction = predict_direction(filtered_frame)

        # サーボモーターの角度を設定
        if direction == 0:  # 左折
            set_servo_angle(52)
            move_motor(0.5, 1)
        elif direction == 1:  # 少し左折
            set_servo_angle(77)
            move_motor(1, 1)
        elif direction == 2:  # 直進
            set_servo_angle(102)
            move_motor(1, 1)
        elif direction == 3:  # 少し右折
            set_servo_angle(127)
            move_motor(1, 1)
        elif direction == 4:  # 右折
            set_servo_angle(152)
            move_motor(1, 0.5)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

prediction_thread = threading.Thread(target=send_predictions, daemon=True)
prediction_thread.start()

try:
    while True:
        pass

except KeyboardInterrupt:
    print("終了します...")

finally:
    cap.release()
    cv2.destroyAllWindows()
    servo.stop()
    GPIO.cleanup()
