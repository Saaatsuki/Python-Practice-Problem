import pygame
import sys

# 初期化
pygame.init()

# 画面の設定
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangles with FPS, Delta Time, and Boundary Check")

# FPSの設定
FPS = 30
clock = pygame.time.Clock()

# 矩形の作成
rect1 = pygame.Rect(100, 100, 50, 50)  # (x, y, width, height)
rect2 = pygame.Rect(150, 150, 50, 50)

# 速度設定（ピクセル/秒）
speed = 200

# メインループ
running = True
while running:
    # デルタタイムの取得
    dt = clock.tick(FPS) / 1000  # 毎フレームの経過時間を秒単位で取得

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キーの状態をチェック
    keys = pygame.key.get_pressed()
    
    # 矩形1の移動
    if keys[pygame.K_LEFT]:
        rect1.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        rect1.x += speed * dt
    if keys[pygame.K_UP]:
        rect1.y -= speed * dt
    if keys[pygame.K_DOWN]:
        rect1.y += speed * dt

    # 矩形2の移動
    if keys[pygame.K_a]:
        rect2.x -= speed * dt
    if keys[pygame.K_d]:
        rect2.x += speed * dt
    if keys[pygame.K_w]:
        rect2.y -= speed * dt
    if keys[pygame.K_s]:
        rect2.y += speed * dt

    # 画面境界のチェックと修正
    if rect1.left < 0:
        rect1.left = 0
    if rect1.right > screen_width:
        rect1.right = screen_width
    if rect1.top < 0:
        rect1.top = 0
    if rect1.bottom > screen_height:
        rect1.bottom = screen_height

    if rect2.left < 0:
        rect2.left = 0
    if rect2.right > screen_width:
        rect2.right = screen_width
    if rect2.top < 0:
        rect2.top = 0
    if rect2.bottom > screen_height:
        rect2.bottom = screen_height

    # 背景の塗りつぶし
    screen.fill((0, 0, 0))

    # 矩形の描画
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 0, 255), rect2)

    # 画面の更新
    pygame.display.flip()

# 終了処理
pygame.quit()
sys.exit()
