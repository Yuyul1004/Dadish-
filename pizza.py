import pygame
import random


class Pizza(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprites = []
        for i in range (1,2):
            current_sprite = pygame.transform.scale(pygame.image.load("enemie 1.png"), (100,100))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x, self.y))