

import pygame

# About position values in pygame
# -> https://stackoverflow.com/questions/62804292/how-to-set-the-position-of-an-image-in-pygame

class Celebration(pygame.sprite.Sprite):
    def __init__(self, kestitsija, width, height , location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer

        self.rect = self.resized_image.get_rect()
        self.rect.x, self.rect.y = location

        



    

    