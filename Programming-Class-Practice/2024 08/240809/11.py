import random
import pygame

pygame.init()

# <<-- 환경 변수 설정
# 화면 사이즈
screen_width = 800
screen_height = 600

# 장애물 사이즈
obs_width = 200
obs_height = 100

# 장애물 개수
num_of_obs = 5

# 아이템 사이즈
item_width = 25
item_height = 25

# 아이템 개수
num_of_item = 10

# 움직이는 사각형 사이즈
moving_rect_width = 50
moving_rect_height = 50
## -->>

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


# 장애물을 랜덤하게 생성
obs_list = []
for _ in range(num_of_obs):
    while True:
        rect_x = random.randint(0, screen_width - obs_width) # 0 <= x <= 600
        rect_y = random.randint(0, screen_height - obs_height) # 0 <= y <= 500
        rect = pygame.Rect(rect_x, rect_y, obs_width, obs_height)
        
        # 새롭게 생성된 장애물 사각형이 기 장애물과 충돌이 없다면
        if rect.collidelist(obs_list) == -1:
            # 새롭게 생성된 장애물을 리스트에 추가
            obs_list.append(rect)
            # 반복문 종료
            break


# 아이템을 랜덤하게 생성
item_list = []
for _ in range(num_of_item):
    while True:
        item_x = random.randint(0, screen_width - item_width)
        item_y = random.randint(0, screen_height - item_height)
        item = pygame.Rect(item_x, item_y, item_width, item_height)
        
        # 아이템과 기 아이템 간 충돌이 없어야 되고 and 아이템과 장애물간 충돌이 없어야 된다
        if item.collidelist(item_list) == -1 and item.collidelist(obs_list) == -1:
            item_list.append(item)
            break

# 움직이는 사각형 만들기
# 장애물과 아이템과 충돌이 일어나지 않는 x, y 값을 설정
mr_x = random.randint(0, screen_width - moving_rect_width)
mr_y = random.randint(0, screen_height - moving_rect_height)
moving_rect = pygame.Rect(mr_x, mr_y, moving_rect_width, moving_rect_height)

while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # -- >> 

    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    # 장애물 그리기
    for rect in obs_list:
        pygame.draw.rect(screen, (255, 0, 0), rect) # Rect 객체 이용
    
    
    # 아이템 그리기
    for rect in item_list:
        pygame.draw.rect(screen, (0, 255, 0), rect)
    
    # 움직이는 사각형 그리기
    pygame.draw.rect(screen, (0, 0, 255), moving_rect)
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


