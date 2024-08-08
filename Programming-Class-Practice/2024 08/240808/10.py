import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("아이템 수집 게임")

# 색상 정의
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 설정
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
ITEM_SIZE = 30
NUM_OBSTACLES = 5
NUM_ITEMS = 5

# 함수 정의
def get_random_position(size):
    return random.randint(0, WIDTH - size), random.randint(0, HEIGHT - size)

def check_collision(rect, others):
    for other in others:
        if rect.colliderect(other):
            return True
    return False

# 장애물 생성
obstacles = []
while len(obstacles) < NUM_OBSTACLES:
    x, y = get_random_position(OBSTACLE_SIZE)
    new_obstacle = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
    if not check_collision(new_obstacle, obstacles):
        obstacles.append(new_obstacle)

# 아이템 생성
items = []
while len(items) < NUM_ITEMS:
    x, y = get_random_position(ITEM_SIZE)
    new_item = pygame.Rect(x, y, ITEM_SIZE, ITEM_SIZE)
    if not check_collision(new_item, obstacles + items):
        items.append(new_item)

# 플레이어 생성
while True:
    x, y = get_random_position(PLAYER_SIZE)
    player = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
    if not check_collision(player, obstacles + items):
        break

# 게임 루프
running = True
clock = pygame.time.Clock()
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -player_speed
    if keys[pygame.K_RIGHT]:
        dx = player_speed
    if keys[pygame.K_UP]:
        dy = -player_speed
    if keys[pygame.K_DOWN]:
        dy = player_speed

    new_player_pos = player.move(dx, dy)
    if not check_collision(new_player_pos, obstacles):
        player = new_player_pos

    collected_items = []
    for item in items:
        if player.colliderect(item):
            collected_items.append(item)

    for item in collected_items:
        items.remove(item)

    # 게임 종료 조건 체크
    if not items:
        print("모든 아이템을 수집했습니다! 승리!")
        running = False

    # 화면 그리기
    window.fill((0, 0, 0))
    pygame.draw.rect(window, RED, player)
    for obstacle in obstacles:
        pygame.draw.rect(window, BLUE, obstacle)
    for item in items:
        pygame.draw.rect(window, YELLOW, item)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
