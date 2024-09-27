import pygame

class Place(pygame.sprite.Sprite):

    def __init__(self,image_file, width, height, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location     

        self.x_pos = 0
        self.y_pos = 0
