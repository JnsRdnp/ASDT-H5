import pygame

# background image in pygame
# -> https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame

class Background(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(1000,450))

        self.rect = self.resized_image.get_rect()
        print(self.rect)
        self.rect.left, self.rect.top = location


