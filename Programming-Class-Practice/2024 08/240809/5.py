import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

rect1 = pygame.Rect(100, 200, 300, 400)

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
    pygame.draw.rect(screen, (255, 0, 0), rect1) # Rect 객체 이용
    
    # 아이템 그리기
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


