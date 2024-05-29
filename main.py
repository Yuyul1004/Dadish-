import pygame
import math


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Dadish")

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#Variables
clock = pygame.time.Clock()
game_speed = 150

#Load images
bg = pygame.image.load("bg.png").convert()
ground_image = pygame.image.load("ground.png")
ground = ground_image.convert_alpha()


# background scrolling
bg_width = bg.get_width()
bg_x = 0

#ground scrolling
ground_x = 0


run = True
# -------- Main Program Loop -----------
while run:

    # --- Main event loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    delta_time = clock.tick(60) / 1000
    bg_x -= game_speed * delta_time
    ground_x -= game_speed * delta_time

    if bg_x < -bg_width:
        bg_x = 0
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + bg_width, 0))

    if ground_x <= -screen_width:
        ground_x = 0
    screen.blit(ground, (ground_x, screen_height - ground.get_height()))
    screen.blit(ground, (ground_x + screen_width, screen_height - ground.get_height()))


    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()