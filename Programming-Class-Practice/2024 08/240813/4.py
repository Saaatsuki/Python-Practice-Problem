import pygame

# 스페이스 키를 누르면 총알이 발사된다.
'''
1. 스페이스 키를 누르면
2. 총알 사각형을 생성
3. 2번에서 생성된 사각형을 플레이어 사각형 Top 중앙에 위치
4. 매 Frame(image) 마다 총알의 y 좌표를 감소 (아래에서 위로 이동)
5. 총알이 화면(Screen) 상단(TOP)을 넘어가면 총알을 삭제
'''

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# 환경 변수
p_rect_width = 80
p_rect_height = 40
f_rect_width = 30
f_rect_height = 30

# 플레이어 사각형 정의
p_rect_x = screen_width // 2 - p_rect_width // 2
p_rect_y = screen_height - p_rect_height - 5
player_rect = pygame.Rect(p_rect_x, p_rect_y, p_rect_width, p_rect_height)


# 객체 이동 속도
speed = 300 # 300 pixel / second

# 총알 사각형을 보관할 리스트 생성
f_rect_list = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_rect = pygame.Rect(0, 0, f_rect_width, f_rect_height)
                # 생성된 사각형을 플레이어 사각형 Top 중앙에 위치
                fire_rect.bottom = player_rect.top
                fire_rect.x = player_rect.centerx - f_rect_width // 2
                # 생성된 총알 사각형을 리스트에 추가
                f_rect_list.append(fire_rect)

    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    

    # 총알 이동 처리
    for f_rect in f_rect_list[:]:
        f_rect.y -= speed * dt
        if f_rect.y < 0:
            f_rect_list.remove(f_rect)
   
    keys = pygame.key.get_pressed()
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed * dt 
        
        
    # 스페이키가 눌러졌을 때
    # if keys[pygame.K_SPACE]:
    # # 총알 사각형을 생성하고
    #     fire_rect = pygame.Rect(0, 0, f_rect_width, f_rect_height)
    #     # 생성된 사각형을 플레이어 사각형 Top 중앙에 위치
    #     fire_rect.bottom = player_rect.top
    #     fire_rect.x = player_rect.centerx - f_rect_width // 2
    #     # 생성된 총알 사각형을 리스트에 추가
    #     f_rect_list.append(fire_rect)
        
    # 화면 경계 처리    
    player_rect.x = max(0, min(player_rect.x, screen.get_width() - player_rect.width))
 
 
    # 화면 그리기 시작
    screen.fill((255, 255, 255))
   
    # 플레이어 사각형 그리기         
    pygame.draw.rect(screen, (0, 0, 255), player_rect) 
   
    # 총알 그리기
    for f_rect in f_rect_list:
        pygame.draw.rect(screen, (255, 0, 0), f_rect) 
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


