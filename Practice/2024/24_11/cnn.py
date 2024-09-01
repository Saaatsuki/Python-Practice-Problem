import os
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# データセットディレクトリのパス
base_dir = 'captured_data'

# カスタムデータセットクラス
class ImageDataset(Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        return torch.tensor(image, dtype=torch.float32).permute(2, 0, 1), torch.tensor(label, dtype=torch.float32)

# データの読み込み関数
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

    return np.array(images, dtype=np.float32) / 255.0, np.array(labels, dtype=np.float32)

# 画像データとラベルをロード
images, labels = load_images(base_dir)

# 訓練データと検証データに分割
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

# データセットとデータローダーを作成
train_dataset = ImageDataset(X_train, y_train)
val_dataset = ImageDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# モデルの定義
class AutonomousCarModel(nn.Module):
    def __init__(self):
        super(AutonomousCarModel, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, activation='relu'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(64, 128, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 6 * 6, 128),
            nn.ReLU(),
            nn.Linear(128, 2)  # 出力: 速度と角度
        )

    def forward(self, x):
        x = self.conv(x)
        x = self.fc(x)
        return x

# モデルのインスタンス
model = AutonomousCarModel()

# 損失関数とオプティマイザ
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# トレーニングループ
num_epochs = 10
train_losses = []
val_losses = []

for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
    train_losses.append(train_loss / len(train_loader))

    # 検証
    model.eval()
    val_loss = 0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
    val_losses.append(val_loss / len(val_loader))

    print(f"Epoch {epoch + 1}/{num_epochs}, Train Loss: {train_losses[-1]:.4f}, Val Loss: {val_losses[-1]:.4f}")

# 学習曲線のプロット
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Validation Loss')
plt.legend()
plt.show()

# モデルの保存
torch.save(model.state_dict(), 'autonomous_car_model.pth')

# 予測関数
def predict_image(image_path, model):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (60, 60))  # CNNに合わせたサイズにリサイズ
    img = np.expand_dims(img, axis=0)  # バッチ次元を追加
    img = torch.tensor(img, dtype=torch.float32).permute(0, 3, 1, 2) / 255.0  # 正規化

    model.eval()
    with torch.no_grad():
        prediction = model(img)
    speed, angle = prediction[0]
    print(f"予測された速度: {speed.item()}, 予測された角度: {angle.item()}")

# 予測の実行
predict_image('captured_data/speed_30/angle_102/0001.jpg', model)
