import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ゲームの状態を更新する処理

    # ゲームの描画を行う処理

    pygame.display.update()
    
    # ゲームの状態を更新する処理
# 例えば、プレイヤーの位置を更新するなど

# ゲームの描画を行う処理
# 例えば、プレイヤーや敵の画像をウィンドウに描画するなど
