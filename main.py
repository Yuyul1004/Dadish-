import pygame
import random
from dadish import Dadish
from pizza import Pizza



pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Dadish")

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#Variables
clock = pygame.time.Clock()
game_speed = 300
display_message = "Space OR Left click to start AND jump"

#Load images
bg = pygame.image.load("bg.png").convert()
ground_image = pygame.image.load("ground.png")
ground = ground_image.convert_alpha()

images = [
    "enemie 1.png"
]

enemy_group = pygame.sprite.Group()
dadish_group = pygame.sprite.GroupSingle()
radish = Dadish(45,307)
dadish_group.add(radish)
pizza = Pizza (1000, 340)

display = font.render(display_message)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = True
                not_run = False
    screen.blit(bg, (0,0))
    screen.blit(radish.image, radish.rect)
    screen.blit(ground_image, (0,0))
    pygame.display.update()
    radish.jump() #jump once to signal start

while run:

    # --- Main event loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                radish.jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            radish.jump()

    delta_time = clock.tick(60) / 1000
    bg_x -= game_speed * delta_time
    ground_x -= game_speed * delta_time
    game_speed += 0.025
    print(game_speed)

    if bg_x < -bg_width:
        bg_x = 0
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + bg_width, 0))


    dadish_group.update()
    dadish_group.draw(screen)

    enemy_group.update()
    enemy_group.draw(screen)

    if ground_x <= -screen_width:
        ground_x = 0
    screen.blit(ground, (ground_x, screen_height - ground.get_height()))
    screen.blit(ground, (ground_x + screen_width, screen_height - ground.get_height()))


    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()