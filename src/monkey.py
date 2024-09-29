import pygame
import time
import random

class Monkey():
    def __init__(self, location, screen, omistaja ,sana=""):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image,(50, 75))
        self.screen = screen
        self.rect = self.resized_image.get_rect()
        self.start_location = location
        self.rect.x, self.rect.y = self.start_location

        self.omistaja = omistaja

        self.apina_mantereella = False
        self.apina_elossa = True

        # Hätäviestin sana apinalle näkymään
        self.text = sana
        self.my_font = pygame.font.SysFont('Comic Sans MS', 17)
        self.text_surface = self.my_font.render(self.text, False, (0, 0, 0))

    def reset_monkey(self):
        self.apina_elossa = True
        self.apina_mantereella = False
        self.rect.x, self.rect.y = self.start_location

    def liikuMantereelle(self, valimatka):
        self.omistaja.lahetetyt_apinat += 1

        kilometri = valimatka / 100  # Lasketaan yhden kilometrin määrä näytöllä

        for step in range(100):
            self.rect.x += kilometri  # Liikutaan yksi kilometri kerallaan sata kertaa
            
            # print(step)

            # Uimisen liikettä ylös alas :D
            if step % 2 != 0:
                self.rect.y += 10
            else:
                self.rect.y -= 10

            time.sleep(0.05)
            # https://docs.python.org/3/library/random.html
            # Prosentin mahdollisuus jokaisella kilometrillä kuolla
            apinan_mahikset= random.randrange(0, 99, 1)

            if apinan_mahikset == 0:
                print("Apina kuoli!")
                self.apina_elossa = False
                return

        if self.apina_elossa == True :
             print("Apina pääsi maihin!")
             self.omistaja.apinat_perilla += 1
             self.apina_mantereella = True
        else :
            print("Hai söi apinan")
        
        # Syntyy uudestaan saarella
        
        
        


    def draw(self,screen):
        self.screen.blit(self.resized_image, self.rect)
        screen.blit(self.text_surface, (self.rect.left, self.rect.bottom+5))