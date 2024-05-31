import pygame



class Dadish(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__() #necessary because there are going to be multiple sprites and makes coding easier because this initializes attributes of parent class)
        self.x = x
        self.y = y
        self.image = pygame.image.load("DADISH_image.png").convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.velocity = 22
        self.gravity = 2
        self.jump_height = 15
        self.is_jumping = False
        self.jump_vel = 0
        #self.ground_level = 305

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_vel = -self.velocity

    def apply_gravity(self):
        if self.is_jumping:
            self.rect.centery += self.jump_vel
            if self.jump_vel < 0:  # Sprite is moving upwards
                self.jump_vel += self.gravity
            else:  # Sprite is moving downwards
                self.jump_vel += self.gravity
            if self.rect.centery >= self.y - self.jump_height:
                self.is_jumping = False
                self.rect.centery = self.y - self.jump_height
                self.jump_vel = 0  # Reset jump velocity
        else:
            if self.rect.centery < self.y:
                self.rect.centery += self.gravity

    def update(self):
        self.apply_gravity()


