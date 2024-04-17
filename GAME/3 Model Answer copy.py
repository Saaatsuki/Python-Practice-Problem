import pygame
import random
import math

# Pygameの初期化
pygame.init()

# 画面の設定
SCREEN_WIDTH = 800  # 画面の幅
SCREEN_HEIGHT = 600  # 画面の高さ
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 画面を作成
pygame.display.set_caption("Space Invaders")  # ゲームのタイトルを設定

# 画像の読み込み
player_img = pygame.image.load("C:/TEST/GAME/player.png")  # プレイヤーの画像
enemy_img = pygame.image.load("C:/TEST/GAME/enemy.png")  # 敵の画像
bullet_img = pygame.image.load("C:/TEST/GAME/bullet.png")  # 弾の画像

# プレイヤーの初期設定
player_width, player_height = player_img.get_size()  # プレイヤー画像のサイズ
player_x = (SCREEN_WIDTH - player_width) // 2  # プレイヤーの初期X座標
player_y = SCREEN_HEIGHT - player_height - 10  # プレイヤーの初期Y座標
player_speed = 12  # プレイヤーの移動速度

# 敵の初期設定
enemy_width, enemy_height = enemy_img.get_size()  # 敵の画像のサイズ
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)  # 敵の初期X座標
enemy_y = random.randint(50, 150)  # 敵の初期Y座標
enemy_speed = 1  # 敵の移動速度

# 弾の初期設定
bullet_width, bullet_height = bullet_img.get_size()  # 弾の画像のサイズ
bullet_x, bullet_y = 0, 480  # 弾の初期座標
bullet_speed = 7  # 弾の速度
bullet_state = "ready"  # 弾の状態（ready: 発射可能, fire: 発射中）

# スコア
score = 0  # スコア
font = pygame.font.SysFont(None, 32)  # フォントの設定

# プレイヤーを描画する関数
def player(x, y):
    screen.blit(player_img, (x, y))

# 敵を描画する関数
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# 弾を発射する関数
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"  # 弾の状態を発射中に設定
    screen.blit(bullet_img, (x + player_width // 2 - bullet_width // 2, y - bullet_height))

# 衝突判定
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)  # ユークリッド距離を計算
    return distance < 27  # 距離が一定以下なら衝突とみなす

# ゲームオーバー処理
def game_over():
    # ゲームオーバーの処理をここに追加する
    pass

# メインのゲームループ
running = True
while running:
    screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # ウィンドウの×ボタンが押されたら終了

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed  # 左キーが押されたらプレイヤーを左に移動
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed  # 右キーが押されたらプレイヤーを右に移動
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x  # 弾のX座標をプレイヤーの位置に設定
                    fire_bullet(bullet_x, bullet_y)  # 弾を発射

    # プレイヤーの移動範囲を画面内に制限
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_width))

    # 敵の移動
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= SCREEN_WIDTH - enemy_width:
        enemy_speed = -enemy_speed
        enemy_y += enemy_height
    if enemy_y > SCREEN_HEIGHT - enemy_height:
        game_over()  # 敵がプレイヤーの領域まで到達したらゲームオーバー

    # 弾の移動
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"  # 弾が画面外に出たら発射可能状態にする

    # 衝突判定
    if isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"  # 衝突したら弾を初期位置に戻し、発射可能状態にする
        score += 1  # スコアを増やす
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)  # 新しい敵をランダムな位置に配置
        enemy_y = random.randint(50, 150)

    # スコアを表示
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # オブジェクトを描画
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    if bullet_state == "fire":
        screen.blit(bullet_img, (bullet_x + player_width // 2 - bullet_width // 2, bullet_y))

    pygame.display.update()  # 画面を更新

# # Pygameの終了処理
# pygame.quit()
