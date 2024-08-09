# import pygame
# import random

# # Pygame 초기화
# pygame.init()

# # 화면 크기 설정
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Falling Square Game")

# # 색상 정의
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # 시계 객체 생성 (프레임 레이트 제어용)
# clock = pygame.time.Clock()

# # 플레이어 사각형 설정
# player_size = 50
# player_x = width // 2 - player_size // 2
# player_y = height - player_size - 10
# player_speed = 10

# # 떨어지는 사각형 리스트 초기화
# falling_squares = []
# falling_speed = 5

# # 게임 시간 설정
# start_time = pygame.time.get_ticks()
# elapsed_time = 0

# # 게임 루프 상태
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # 키 입력 처리
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[pygame.K_RIGHT] and player_x < width - player_size:
#         player_x += player_speed

#     # 화면을 흰색으로 지우기
#     screen.fill(white)
    
#     # 플레이어 그리기
#     pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))

# # 1초마다 이벤트 발생 (사각형 생성)
# falling_square_event = pygame.USEREVENT + 1
# pygame.time.set_timer(falling_square_event, 1000)

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == falling_square_event:
#             for _ in range(random.randint(1, 5)):
#                 square_x = random.randint(0, width - player_size)
#                 square_y = 0
#                 falling_squares.append([square_x, square_y])

#     # 사각형 업데이트
#     for square in falling_squares:
#         square[1] += falling_speed

#     # 화면을 흰색으로 지우기
#     screen.fill(white)
    
#     # 플레이어 그리기
#     pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    
#     # 떨어지는 사각형 그리기
#     for square in falling_squares:
#         pygame.draw.rect(screen, red, (square[0], square[1], player_size, player_size))

#     # 충돌 감지
#     for square in falling_squares:
#         if player_x < square[0] + player_size and player_x + player_size > square[0] and player_y < square[1] + player_size and player_y + player_size > square[1]:
#             print("충돌 발생! 게임 종료")
#             running = False

#     # 경과 시간 계산
#     elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    
#     # 경과 시간 표시
#     font = pygame.font.Font(None, 36)
#     time_text = font.render(f"Time: {elapsed_time:.2f} sec", True, black)
#     screen.blit(time_text, (10, 10))
    
#     # 30초 동안 생존 시 승리
#     if elapsed_time >= 30:
#         print("30초 동안 생존! 승리")
#         running = False

import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Square Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 10

falling_squares = []
falling_speed = 5

start_time = pygame.time.get_ticks()

falling_square_event = pygame.USEREVENT + 1
pygame.time.set_timer(falling_square_event, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == falling_square_event:
            for _ in range(random.randint(1, 5)):
                square_x = random.randint(0, width - player_size)
                square_y = 0
                falling_squares.append([square_x, square_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    for square in falling_squares:
        square[1] += falling_speed

    screen.fill(white)
    
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    
    for square in falling_squares:
        pygame.draw.rect(screen, red, (square[0], square[1], player_size, player_size))

    for square in falling_squares:
        if player_x < square[0] + player_size and player_x + player_size > square[0] and player_y < square[1] + player_size and player_y + player_size > square[1]:
            print("충돌 발생! 게임 종료")
            running = False

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    font = pygame.font.Font(None, 36)
    time_text = font.render(f"Time: {elapsed_time:.2f} sec", True, black)
    screen.blit(time_text, (10, 10))
    
    if elapsed_time >= 30:
        print("30초 동안 생존! 승리")
        running = False
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

