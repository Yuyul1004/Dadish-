import pygame
from dadish import Dadish



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

dadish_group = pygame.sprite.GroupSingle()
radish = Dadish(45,313)
dadish_group.add(radish)


# background scrolling
bg_width = bg.get_width()
bg_x = 0

#ground scrolling
ground_x = 0

not_run = True
run = False
# -------- Main Program Loop -----------
while not_run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            not_run = False
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = True
            not_run = False
    screen.blit(bg, (0,0))
    screen.blit(radish.image, radish.rect)
    screen.blit(ground_image, (0,0))
    pygame.display.update()

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

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            radish.jump()

    dadish_group.update()
    dadish_group.draw(screen)

    if ground_x <= -screen_width:
        ground_x = 0
    screen.blit(ground, (ground_x, screen_height - ground.get_height()))
    screen.blit(ground, (ground_x + screen_width, screen_height - ground.get_height()))


    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()