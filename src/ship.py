import pygame
import time
import random

class Ship():
    def __init__(self, screen, omistaja):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/laiva.png")
        self.resized_image = pygame.transform.scale(self.image,(120, 100))

        self.screen = screen
        self.rect = self.resized_image.get_rect()

        # Aloituspaikka omistajan vieressä
        self.omistaja = omistaja
        self.start_location = [self.omistaja.rect.centerx-150,self.omistaja.rect.top-50]
        self.rect.x, self.rect.y = self.start_location


    def liikuSaarelle(self, valimatka):

        kilometri = valimatka / 100  

        for step in range(100):
            self.rect.x -= kilometri  # Liikutaan yksi kilometri kerallaan sata kertaa
            
            # print(step)

            # Veneen liikettä ylös alas :D
            if step % 2 != 0:
                self.rect.y += 10
            else:
                self.rect.y -= 10

            time.sleep(0.05)

    def draw(self,screen):
        self.screen.blit(self.resized_image, self.rect)