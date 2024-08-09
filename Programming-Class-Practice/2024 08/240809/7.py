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
## -->>

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


# 장애물을 랜덤하게 생성
obs_list = []
for _ in range(num_of_obs):
    rect_x = random.randint(0, screen_width - obs_width) # 0 <= x <= 600
    rect_y = random.randint(0, screen_height - obs_height) # 0 <= y <= 500
    rect1 = pygame.Rect(rect_x, rect_y, obs_width, obs_height)
    obs_list.append(rect1)


# 아이템을 랜덤하게 생성


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
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


