import pygame

# 色を定義 (RGB形式)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pygameを初期化
pygame.init()
# 画面のサイズを設定
screen = pygame.display.set_mode((800, 600))
# クロックオブジェクトを作成 (フレームレート制御に使用)
clock = pygame.time.Clock()

# 円の初期位置と半径、速度を設定
x = screen.get_width() / 2  # 画面の幅の中央
y = screen.get_height() / 2  # 画面の高さの中央
radius = 40  # 円の半径
speed = 5  # 移動速度

# メインループのフラグ
running = True
while running:
    # イベントを処理
    for event in pygame.event.get():
        # 終了イベントが発生した場合、ループを終了
        if event.type == pygame.QUIT:
            running = False

    # 画面を白で塗りつぶす
    screen.fill((255, 255, 255))
    
    # 円を描画 (色は赤、位置は(x, y)、半径はradius)
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    # 画面の端に到達した場合、速度の方向を反転
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
    
    # x座標を更新 (円を移動)
    x += speed

    # 画面を更新
    pygame.display.flip()
    
    # フレームレートを制御 (1秒間に120フレーム)
    clock.tick(120)
    
# Pygameを終了
pygame.quit()
