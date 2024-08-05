import pygame


#  초기화
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
x = 50
y = 240
speed = 5

# 이벤트처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)
    
# 종료
pygame.quit()
