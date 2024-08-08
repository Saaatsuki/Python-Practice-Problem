import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)

while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("마우스 버튼 다운")
        elif event.type == pygame.MOUSEBUTTONUP:
            print("마우스 버튼 업")
        elif event.type == pygame.MOUSEMOTION:
            rect1.x = event.pos[0]
            rect1.y = event.pos[1]
    # -- >> 

    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


