import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 장애물을 랜덤하게 생성
rect_x = random.randint(0, 800 - 200) # 0 <= x <= 600
rect_y = random.randint(0, 600 - 100) # 0 <= y <= 500

rect1 = pygame.Rect(rect_x, rect_y, 200, 100)

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
    pygame.draw.rect(screen, (255, 0, 0), rect1) # Rect 객체 이용
    
    # 아이템 그리기
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


