import pygame
import time
import random
import winsound


# monta ääntä päällekäin https://stackoverflow.com/questions/53617967/play-music-and-sound-effects-on-top-of-each-other-pygame

class Monkey():
    def __init__(self, screen, omistaja ,sana="", saapuneet_sanat=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image,(50, 75))
        self.screen = screen
        self.rect = self.resized_image.get_rect()

        # Hai kuva kuolemista varteen
        self.sharkimage = pygame.image.load("./assets/shark.png")
        self.resized_sharkimage = pygame.transform.scale(self.sharkimage,(50, 75))
        self.shark_rect = self.resized_sharkimage.get_rect()
        self.shark_rect.x, self.shark_rect.y = [100, 100]

        # Aloituspaikka omistajan vieressä
        self.omistaja = omistaja
        self.start_location = [self.omistaja.rect.centerx+10,self.omistaja.rect.top]
        self.rect.x, self.rect.y = self.start_location

        self.apina_mantereella = False
        self.apina_elossa = True

        
        self.saapuneet_sanat = saapuneet_sanat

        # Hätäviestin sana apinalle näkymään
        self.text = sana
        self.my_font = pygame.font.SysFont('Comic Sans MS', 17)
        self.text_surface = self.my_font.render(self.text, False, (0, 0, 0))

        # Ääniä
        self.splash_sound = pygame.mixer.Sound("./assets/splash.wav")
        self.splash_sound.set_volume(0.05)
        self.success_sound = pygame.mixer.Sound("./assets/success.wav")
        self.chomp_sound = pygame.mixer.Sound("./assets/chomp.wav")

    def reset_monkey(self):
        self.apina_elossa = True
        self.apina_mantereella = False
        self.rect.x, self.rect.y = self.start_location

    def liikuMantereelle(self, valimatka, vastaanottajavahdissa=False):
        self.omistaja.lahetetyt_apinat += 1

        kilometri = valimatka / 100  # Lasketaan yhden kilometrin määrä näytöllä


        for step in range(100):


            # pygame.mixer.Sound.play(self.splash_sound)

            self.rect.x += kilometri  # Liikutaan yksi kilometri kerallaan sata kertaa

            # Uimisen liikettä ylös alas :D
            if step % 2 != 0:
                self.rect.y += 10
            else:
                self.rect.y -= 10

            time.sleep(0.05)
            # https://docs.python.org/3/library/random.html

            
            apinan_mahikset= random.randint(1, 145)

            # Jos arvottu numero on 100, apina kuolee
            if apinan_mahikset == 100:
                # print("Apina kuoli!")
                self.apina_elossa = False
                pygame.mixer.Sound.play(self.chomp_sound)
                return

        if self.apina_elossa == True:
            # print("Apina pääsi maihin!")
            self.omistaja.apinat_perilla += 1
            self.apina_mantereella = True

            pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.success_sound), maxtime=1000)

            # Päivitetään sanalistaa mitä mantereelle on päässyt
            if self.saapuneet_sanat is not None and self.text not in self.saapuneet_sanat and vastaanottajavahdissa:
                self.saapuneet_sanat.append(self.text)
                print("Lisättiin sana saapuneisin")

        else:
            # Tämä ääni ei jostain syystä toimi
            self.apina_elossa = False
            print("Hai söi apinan")
        
        # Syntyy uudestaan saarella
        

    def draw(self,screen):

        if self.apina_elossa == True:
            screen.blit(self.resized_image, self.rect)
            screen.blit(self.text_surface, (self.rect.left, self.rect.bottom+5))
        else:
            self.shark_rect.x, self.shark_rect.y = self.rect.x, self.rect.y
            screen.blit(self.resized_sharkimage, self.shark_rect)
            screen.blit(self.text_surface, (self.rect.left, self.rect.bottom+5))