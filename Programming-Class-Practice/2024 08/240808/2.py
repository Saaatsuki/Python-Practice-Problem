import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("마우스 버튼 다운")
        elif event.type == pygame.MOUSEBUTTONUP:
            print("마우스 버튼 업")
    # -- >> 

    # <<-- 화면 그리기
    screen.fill((0, 0, 0))
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


