import pygame

# Pygameの初期化
pygame.init()

# 640x480ピクセルの画面を作成
screen = pygame.display.set_mode((640,480))
# ウィンドウのタイトルを設定
pygame.display.set_caption("Rectangular Drawing")

# カラー定義（白、青、赤）
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

# 一つ目の矩形の定義（位置: x=100, y=100、幅=100、高さ=50）
rect1 = pygame.Rect(100,100,100,50)

# メインループの開始
running = True 
while running:
    # イベント処理ループ
    for event in pygame.event.get():
        # 終了イベント（ウィンドウを閉じる操作）があればループを終了
        if event.type == pygame.QUIT:
            running = False

    # 画面を白で塗りつぶす
    screen.fill(white)

    # 青い矩形を描画
    pygame.draw.rect(screen,blue,rect1)
    # 赤い矩形を描画（位置: x=200, y=200、幅=50、高さ=100）
    pygame.draw.rect(screen,red,(200,200,50,100))

    # 画面更新
    pygame.display.flip()

# Pygameの終了処理
pygame.quit()
