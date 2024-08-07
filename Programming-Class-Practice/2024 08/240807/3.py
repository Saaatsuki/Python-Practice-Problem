import pygame

# Pygameの初期化
pygame.init()

# 画面のサイズ設定
screen = pygame.display.set_mode((800, 600))
# 時計の初期化（フレームレート制御用）
clock = pygame.time.Clock()
# ゲームループのフラグ
running = True

# 矩形の定義（画面の中央に配置）
rect1 = pygame.Rect(screen.get_width() / 2 - 40, 0, 80, 40)

# 矩形の移動速度（ピクセル/秒）
speed = 300

# クリックカウントの初期化
count = 0

# ゲームループ
while running:
    # イベントの処理
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンが押されたとき
        if event.type == pygame.QUIT:
            running = False
        # キーボードのキーが押されたとき
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("左矢印キーが押されました: ", count)
                count += 1

    # フレームレート制御と経過時間の取得（秒単位）
    dt = clock.tick(60) / 1000

    # キーボード入力の処理
    keys = pygame.key.get_pressed()
    
    # 左キーが押されたとき
    if keys[pygame.K_LEFT]:
        print("左矢印キーが押されました: ", count)
        count += 1

    # 矩形を上下に移動させるコード（コメントアウトされています）
    rect1.y += speed * dt
    if rect1.bottom > screen.get_height():
        rect1.y = screen.get_height() - rect1.height
        speed = -speed
    if rect1.y < 0:
        rect1.y = 0
        speed = -speed
    
    # 矩形を左右に移動させるコード（コメントアウトされています）
    rect1.x += speed * dt
    if rect1.right > screen.get_width():
        rect1.x = screen.get_width() - rect1.width
        speed = -speed
    if rect1.x < 0:
        rect1.x = 0
        speed = -speed
    
    # 画面を白色で塗りつぶす
    screen.fill((255, 255, 255))

    # 矩形を描画（青色）
    pygame.draw.rect(screen, (0, 0, 255), rect1)
    
    # 描画した内容を画面に反映
    pygame.display.flip()

# Pygameの終了
pygame.quit()
