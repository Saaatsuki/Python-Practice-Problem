import random
import pygame

pygame.init()

screen_width = 800
screen_height = 600
obs_width = 100
obs_height = 50
num_of_obs = 10

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

obs_list = []
# 사각형을 3개 생성
for _ in range(num_of_obs):
    while True:
        # 사각형을 랜덤한 위치에 생성
        rect1_x = random.randint(0, screen_width - obs_width) # 0 ~ 540 X
        rect1_y = random.randint(0, screen_height - obs_height ) # 0 ~ 430 Y
        rect = pygame.Rect(rect1_x, rect1_y, 100, 50)
        
        # 생성된 사각형이 기존 사각형의 충돌이 일어나지 않을 경우
        if rect.collidelist(obs_list) == -1:
           # 생성된 사각형을 리스트에 추가
           obs_list.append(rect)
           break



while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # -- >> 

    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    for rect in obs_list:
        pygame.draw.rect(screen, (255, 0, 0), rect) # Rect 객체 이용
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


