import pygame



class Dadish(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__() #necessary because there are going to be multiple sprites and makes coding easier because this initializes attributes of parent class)
        self.x = x
        self.y = y
        self.image = pygame.image.load("DADISH_image.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.velocity = 50
        self.gravity = 4.5

    def jump(self):
        if self.rect.centery >=360:
            while self.rect.centery- self.velocity > 40:
                self.rect.centery -= 1
    def apply_gravity(self):
        if self.rect.centery <=360:
            self.rect.centery += self.gravity
    def update(self):
        self.apply_gravity()


