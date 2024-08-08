import pygame
import random

# 初期化
pygame.init()

# 画面のサイズを設定
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("アイテム収集ゲーム")

# 色の定義
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 設定
PLAYER_SIZE = 50  # プレイヤーの大きさ
OBSTACLE_SIZE = 50  # 障害物の大きさ
ITEM_SIZE = 30  # アイテムの大きさ
NUM_OBSTACLES = 5  # 障害物の数
NUM_ITEMS = 5  # アイテムの数

# 関数定義
def get_random_position(size):
    # 指定されたサイズのオブジェクトを画面内のランダムな位置に配置するための座標を返す
    return random.randint(0, WIDTH - size), random.randint(0, HEIGHT - size)

def check_collision(rect, others):
    # 指定された矩形(rect)がリスト内の他の矩形(others)と衝突しているかを確認する
    for other in others:
        if rect.colliderect(other):
            return True
    return False

# 障害物の生成
obstacles = []
while len(obstacles) < NUM_OBSTACLES:
    x, y = get_random_position(OBSTACLE_SIZE)
    new_obstacle = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
    if not check_collision(new_obstacle, obstacles):
        obstacles.append(new_obstacle)

# アイテムの生成
items = []
while len(items) < NUM_ITEMS:
    x, y = get_random_position(ITEM_SIZE)
    new_item = pygame.Rect(x, y, ITEM_SIZE, ITEM_SIZE)
    if not check_collision(new_item, obstacles + items):
        items.append(new_item)

# プレイヤーの生成
while True:
    x, y = get_random_position(PLAYER_SIZE)
    player = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
    if not check_collision(player, obstacles + items):
        break

# ゲームループ
running = True
clock = pygame.time.Clock()
player_speed = 5  # プレイヤーの移動速度

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -player_speed  # 左キーを押すと左に移動
    if keys[pygame.K_RIGHT]:
        dx = player_speed  # 右キーを押すと右に移動
    if keys[pygame.K_UP]:
        dy = -player_speed  # 上キーを押すと上に移動
    if keys[pygame.K_DOWN]:
        dy = player_speed  # 下キーを押すと下に移動

    new_player_pos = player.move(dx, dy)
    if not check_collision(new_player_pos, obstacles):
        player = new_player_pos

    collected_items = []
    for item in items:
        if player.colliderect(item):
            collected_items.append(item)

    for item in collected_items:
        items.remove(item)

    # ゲーム終了条件のチェック
    if not items:
        print("すべてのアイテムを収集しました！勝利！")
        running = False

    # 画面の描画
    window.fill((0, 0, 0))
    pygame.draw.rect(window, RED, player)
    for obstacle in obstacles:
        pygame.draw.rect(window, BLUE, obstacle)
    for item in items:
        pygame.draw.rect(window, YELLOW, item)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
