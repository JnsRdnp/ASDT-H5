

import pygame

# About position values in pygame
# -> https://stackoverflow.com/questions/62804292/how-to-set-the-position-of-an-image-in-pygame

class Celebration(pygame.sprite.Sprite):
    def __init__(self, kestitsija, fontsize):

        self.pirskeiden_pitaja = kestitsija

        self.my_font = pygame.font.SysFont('Comic Sans MS', fontsize)

        self.selvinneet_apinat = kestitsija.apinat_perilla
        self.ruokitut_suut = self.selvinneet_apinat * 4
        self.pippuria_kaytetty_tl = self.selvinneet_apinat*2

        # 1 apina
        # 2 kg perunoita
        # 3 dl kuohukermaa
        # 2 tl mustapippuria
        # 1 tl suolaa



    def draw(self,screen):
        self.text_surface = self.my_font.render(f"Juhlissa suita ruokittu: {self.ruokitut_suut}\n Pippuria käytetty: {self.pippuria_kaytetty_tl} tl", False, (255, 0, 0))
        screen.blit(self.text_surface, (self.pirskeiden_pitaja.rect.centerx, self.pirskeiden_pitaja.rect.centerx - 100))
        print("Piiretään juhlat")


    

    