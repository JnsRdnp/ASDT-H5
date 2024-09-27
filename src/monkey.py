import pygame
import time

class Monkey():
    def __init__(self, image_file, width, height , location, screen, update_screen_func):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(width, height))
        self.screen = screen
        self.rect = self.resized_image.get_rect()
        self.rect.x, self.rect.y = location

        self.update_screen_func = update_screen_func  # Store the update function

    def liikuMantereelle(self, valimatka):
        for i in range(0,valimatka+5,5):
            self.rect.x += 5
            print(i)
            self.update_screen_func()

    def liikuSaarelle(self, valimatka):
        for i in range(0,-valimatka-5,-5):
            print(i)

    def draw(self):
        self.screen.blit(self.resized_image, self.rect)