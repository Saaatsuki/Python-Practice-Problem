import pygame
from pygame import mixer

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Invaders Game")

# Load player image
player_img = pygame.image.load("C:/TEST/GAME/player.png")
player_width, player_height = player_img.get_size()
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10  # Adjusted to fit at the bottom
playerX_cange = 0


# Load sounds
mixer.init()
laser_sound = mixer.Sound("C:/TEST/GAME/laser.wav")

def player(player_x, player_y):
    screen.blit(player_img, (player_x, player_y))



clock = pygame.time.Clock()
running = True
while running:
    screen.fill((150, 150, 150))

    font = pygame.font.SysFont(None, 36)
    message = font.render("WELCOME!!", True, (255, 255, 255))
    screen.blit(message, (20, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handling key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                player_x += 5
            elif event.key == pygame.K_SPACE:
                laser_sound.play()

    # Keep player within screen boundaries
    player_x = max(0, min(player_x, screen_width - player_width))

    pygame.display.update()
    clock.tick(60)  # Limit frame rate to 60 FPS

player(player_x,player_y)
pygame.quit()
