import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)

# 객체 이동 속도
speed = 300 # 300 pixel / second

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    
    
    keys = pygame.key.get_pressed()
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        rect1.x = rect1.x - speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        rect1.x += speed * dt 
        
    # 아래쪽 방향키가 눌러졌을 때
    if keys[pygame.K_DOWN]:
        rect1.y += speed * dt
    
    # 위쪽 방향키가 눌러졌을 때
    if keys[pygame.K_UP]:
        rect1.y -= speed * dt
        
    # 오른쪽 경계 처리
    if rect1.x + rect1.width > screen.get_width():
        rect1.x = screen.get_width() - rect1.width
    
    # 왼쪽 경계 처리
    if rect1.x < 0:
        rect1.x = 0
    
    # 위쪽 경계 처리
    if rect1.y < 0:
        rect1.y = 0
    
    # 아래쪽 경계 처리
    if rect1.y + rect1.height > screen.get_height():
        rect1.y = screen.get_height() - rect1.height
        
        
    
    
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


