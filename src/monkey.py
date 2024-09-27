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
        # Apina liikkuu matkan pätkissä että pätkiä tulee sata

        kilometri = int(valimatka/100)
        for i in range(0,valimatka+5, kilometri):
            self.rect.x += kilometri
            
            # Uimisen liikettä :D
            if i%10 != 0:
                self.rect.y += 10
            else:
                self.rect.y -= 10

            self.update_screen_func()
            time.sleep(0.05)

    def liikuSaarelle(self, valimatka):
        kilometri = int(valimatka/100)
        for i in range(0,-valimatka-5,kilometri):
            self.rect.x -= kilometri
            print(i)
            
            self.update_screen_func()
            time.sleep(0.05)

    def draw(self):
        self.screen.blit(self.resized_image, self.rect)