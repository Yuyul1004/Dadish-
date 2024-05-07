import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Dadish")

size = (1000, 500)
screen = pygame.display.set_mode(size)

run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

