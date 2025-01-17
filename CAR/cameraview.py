import cv2

# USBカメラを開く（通常 /dev/video0 に接続される）
cap = cv2.VideoCapture(0)  # 0はカメラデバイス番号

if not cap.isOpened():
    print("カメラを開けませんでした")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした")
        break

    cv2.imshow("USB Camera", frame)

    # 'q'キーを押して終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
