import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 게임 변수
fall_rect_width = 80
fall_rect_height = 40


# 떨어지는 사각형
rect = pygame.Rect(0 , 0, fall_rect_width, fall_rect_height)

# 객체 이동 속도
speed = 100 # 300 pixel / second

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  

    # 떨어지는 사각형의 y값 증가
    rect.y += speed * dt
    
    # 화면 그리기
    screen.fill((255, 255, 255))
            
    pygame.draw.rect(screen, (0, 0, 255), rect) 
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
pygame.quit()


