import torch
import torch.nn as nn
import torch.optim as optim
import os
from torchvision import transforms, datasets
from torch.utils.data import DataLoader, random_split
from PIL import Image

# 1. データ準備
transform = transforms.Compose([
    transforms.Resize((60, 60)),  
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

data_path = "CAR/speed_30"  # 実際のデータセットのパス

dataset = datasets.ImageFolder(data_path, transform=transform)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# 2. モデル定義
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 5)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)  # Flatten
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = CNNModel()

# 3. 損失関数とオプティマイザ
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. 学習ループ
num_epochs = 10
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {running_loss / len(train_loader)}")

# 5. モデルの保存
model_save_path = "CAR/speed_30/trained_model.pth"
torch.save(model.state_dict(), model_save_path)
print(f"Model saved to {model_save_path}")

# 6. 予測結果の保存
model.eval()  # 評価モードに切り替え
output_dir = "CAR/speed_30/outputs"
os.makedirs(output_dir, exist_ok=True)  # 出力ディレクトリを作成

correct = 0
total = 0

with torch.no_grad():
    for idx, (images, labels) in enumerate(test_loader):
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        # 予測結果を保存（画像と予測ラベル）
        for i in range(images.size(0)):
            image = images[i].cpu().numpy().transpose((1, 2, 0))  # (C, H, W) から (H, W, C) に変換
            image = (image * 0.5) + 0.5  # 正規化を逆転
            image = Image.fromarray((image * 255).astype('uint8'))  # 画像を保存
            predicted_label = predicted[i].item()
            output_path = os.path.join(output_dir, f"image_{idx * 32 + i}_pred_{predicted_label}.jpg")
            image.save(output_path)

# 精度を表示
print(f"Accuracy: {100 * correct / total}%")
