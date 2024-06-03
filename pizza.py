import pygame


class Pizza(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemie 1.png").convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))