import pygame
import math

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Dadish")

clock = pygame.time.Clock()
fps = 50

screen_width = 1100
screen_length = 500
screen = pygame.display.set_mode((screen_width, screen_length))

# load image
bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()


tiles = math.ceil(screen_width/bg_width)
print(tiles)


run = True

# -------- Main Program Loop -----------
while run:

    clock.tick(fps)
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width, 0))



    # --- Main event loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    #keys = pygame.key.get_pressed()

        if event.type ==


    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()