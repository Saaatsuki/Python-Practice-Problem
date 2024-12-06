import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# データセットディレクトリのパス
base_dir = 'captured_data'

def load_images(base_dir):
    images = []
    labels = []
    for speed_dir in os.listdir(base_dir):
        speed_path = os.path.join(base_dir, speed_dir)
        if os.path.isdir(speed_path):
            for angle_dir in os.listdir(speed_path):
                angle_path = os.path.join(speed_path, angle_dir)
                if os.path.isdir(angle_path):
                    for img_name in os.listdir(angle_path):
                        img_path = os.path.join(angle_path, img_name)
                        if img_path.endswith(".jpg"):
                            # 画像の読み込み
                            img = cv2.imread(img_path)
                            img = cv2.resize(img, (60, 60))  # CNNに合わせたサイズにリサイズ
                            images.append(img)

                            # ラベル (speed, angle)
                            speed = int(speed_dir.split('_')[1])
                            angle = int(angle_dir.split('_')[1])
                            labels.append([speed, angle])  # speedとangleをラベルとして保存

    return np.array(images), np.array(labels)

# 画像データとラベルをロード
images, labels = load_images(base_dir)

# データの正規化
images = images.astype('float32') / 255.0

# ラベルの分割 (速度と角度を別々に分類する場合)
y_speed = labels[:, 0]  # 速度のラベル
y_angle = labels[:, 1]  # 角度のラベル

def build_model():
    model = Sequential()

    # 畳み込み層とプーリング層を追加
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(60, 60, 3)))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2))  # 出力層：2つの値（速度、角度）を予測

    model.compile(optimizer=Adam(), loss='mean_squared_error')
    return model

# モデルの構築
model = build_model()
model.summary()

# 訓練データと検証データに分割
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

# モデルの訓練
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# 訓練結果を表示
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# 訓練したモデルを保存
model.save('autonomous_car_model.h5')

# 新しい画像に対して予測
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (60, 60))  # CNNに合わせたサイズにリサイズ
    img = np.expand_dims(img, axis=0)  # バッチ次元を追加
    img = img.astype('float32') / 255.0  # 正規化

    prediction = model.predict(img)
    speed, angle = prediction[0]
    print(f"予測された速度: {speed}, 予測された角度: {angle}")

# 予測の実行
predict_image('captured_data/speed_30/angle_102/0001.jpg')