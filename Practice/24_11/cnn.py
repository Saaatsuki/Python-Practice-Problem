# pip install tensorflow keras numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

# モデルの準備
model = Sequential()

# 1つ目の畳み込み層
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 2つ目の畳み込み層
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 3つ目の畳み込み層
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# フラット化（1次元に変換）
model.add(Flatten())

# 全結合層
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # 1つの出力（車かそうでないか）

# モデルのコンパイル
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# 学習用の画像データを用意する
# ここではImageDataGeneratorを使って画像を読み込む
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'data/train',  # トレーニング用の画像が保存されたフォルダ
    target_size=(64, 64),  # 画像サイズを統一
    batch_size=32,
    class_mode='binary')  # 2クラス（車か車じゃないか）

validation_generator = test_datagen.flow_from_directory(
    'data/validation',  # 検証用の画像が保存されたフォルダ
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# モデルの学習
model.fit(
    train_generator,
    steps_per_epoch=100,  # 学習ステップ数
    epochs=10,            # 学習回数
    validation_data=validation_generator,
    validation_steps=50)  # 検証ステップ数

# モデルを保存
model.save('car_recognition_model.h5')

# モデルの評価
scores = model.evaluate(validation_generator)
print(f"Accuracy: {scores[1]*100}%")

# 学習の進行状況をグラフで表示
history = model.history

# 正解率の推移をプロット
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legand(loc='lower right')
plt.show()

# 新しい画像で予測
from keras.preprocessing import image

# 新しい画像を読み込む
img_path = 'path_to_new_car_image.jpg'  # 新しい画像のパスを指定
img = image.load_img(img_path, target_size=(64, 64))

# 画像を配列に変換
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # ピクセル値を0~1にスケーリング

# モデルを使って予測
prediction = model.predict(img_array)

# 結果を表示
if prediction[0] > 0.5:
    print("この画像は車です！")
else:
    print("この画像は車ではありません。")