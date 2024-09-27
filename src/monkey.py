import pygame
from person import Person
import time

# Monkey perii ihmisluokan
class Monkey(Person):
    def __init__(self, image_file, width, height , location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.x, self.rect.y = location

    def liikuMantereelle(self, valimatka):
        for i in range(0,valimatka+5,5):
            self.rect.x += 5
            print(i)
            pygame.display.flip()

    def liikuSaarelle(self, valimatka):
        for i in range(0,-valimatka-5,-5):
            print(i)