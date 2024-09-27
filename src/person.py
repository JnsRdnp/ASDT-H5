import pygame

# About position values in pygame
# -> https://stackoverflow.com/questions/62804292/how-to-set-the-position-of-an-image-in-pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, image_file, width, height , initial_x, initial_y):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y

        # self.rect.left, self.rect.top = 