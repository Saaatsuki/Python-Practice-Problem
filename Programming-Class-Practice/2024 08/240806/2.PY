import pygame

# 初期化
pygame.init()

# 画面の設定
screen = pygame.display.set_mode((800, 600))

# 矩形の作成
rect1 = pygame.Rect(100, 100, 50, 50)  # (x, y, width, height)
rect2 = pygame.Rect(150, 150, 50, 50)

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 背景の塗りつぶし
    screen.fill((0, 0, 0))

    # 矩形の描画
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)

    # 衝突検知
    if rect1.colliderect(rect2):
        print("衝突しています！")

    # 画面の更新
    pygame.display.flip()

# 終了処理
pygame.quit()
