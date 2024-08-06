import pygame
import sys
import random

# 初期化
pygame.init()

# 画面の設定
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Timer Example")

# FPSの設定
FPS = 30
clock = pygame.time.Clock()

# フォントの設定
font = pygame.font.Font(None, 36)

# カスタムイベントの定義
SPAWN_BLUE_RECT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLUE_RECT, 1000)  # 1秒ごとにイベントを発生させる

# 矩形の初期設定
red_rect = pygame.Rect(100, 100, 50, 50)  # (x, y, width, height)
blue_rects = []

# 速度設定（ピクセル/秒）
speed = 200

# ゲームの開始時間
start_time = pygame.time.get_ticks()

# メインループ
running = True
while running:
    # デルタタイムの取得
    dt = clock.tick(FPS) / 1000  # 毎フレームの経過時間を秒単位で取得

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_BLUE_RECT:
            # 青い矩形をランダムな位置に生成
            x = random.randint(0, screen_width - 50)
            y = random.randint(0, screen_height - 50)
            blue_rects.append(pygame.Rect(x, y, 50, 50))

    # キーの状態をチェック
    keys = pygame.key.get_pressed()
    
    # 赤い矩形の移動
    if keys[pygame.K_LEFT]:
        red_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        red_rect.x += speed * dt
    if keys[pygame.K_UP]:
        red_rect.y -= speed * dt
    if keys[pygame.K_DOWN]:
        red_rect.y += speed * dt

    # 画面境界のチェックと修正（赤い矩形）
    if red_rect.left < 0:
        red_rect.left = 0
    if red_rect.right > screen_width:
        red_rect.right = screen_width
    if red_rect.top < 0:
        red_rect.top = 0
    if red_rect.bottom > screen_height:
        red_rect.bottom = screen_height

    # 背景の塗りつぶし
    screen.fill((0, 0, 0))

    # 矩形の描画
    pygame.draw.rect(screen, (255, 0, 0), red_rect)
    for rect in blue_rects:
        pygame.draw.rect(screen, (0, 0, 255), rect)

    # 経過時間の計算
    elapsed_time_ms = pygame.time.get_ticks() - start_time
    elapsed_time_sec = elapsed_time_ms / 1000

    # 経過時間の表示
    timer_text = font.render(f"Time: {elapsed_time_sec:.2f} seconds", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    # 30秒後にゲームを終了
    if elapsed_time_sec > 30:
        running = False

    # 画面の更新
    pygame.display.flip()

# 終了処理
pygame.quit()
sys.exit()
