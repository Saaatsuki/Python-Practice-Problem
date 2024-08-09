import random
import pygame

pygame.init()

screen_width = 640
screen_height = 480
obs_width = 100
obs_height = 50

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

rect1_x = random.randint(0, screen_width - obs_width) # 0 ~ 540 X
rect1_y = random.randint(0, screen_height - obs_height ) # 0 ~ 430 Y
rect1 = pygame.Rect(rect1_x, rect1_y, 100, 50)


while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False
    # -- >> 

    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), rect1) # Rect 객체 이용
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


