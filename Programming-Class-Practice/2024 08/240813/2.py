import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 플레이어 사각형 정의
player_rect = pygame.Rect(0, 0, 80, 40)


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
        player_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed * dt 
        
    
    # 화면 경계 처리    
    player_rect.x = max(0, min(player_rect.x, screen.get_width() - player_rect.width))


 
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))
   
    # 플레이어 사각형 그리기         
    pygame.draw.rect(screen, (0, 0, 255), player_rect) 
   
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


