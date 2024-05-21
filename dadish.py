import pygame



class Dadish:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("DADISH_image.png")
        #self.w = self.image.get_width()
        #self.h = self.image.get_height()
        self.image_size = self.image.get_size()
        #self.image_size = pygame.transform.scale( self.image, ((self.w * 5),(self.h * 5)))
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .2

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

