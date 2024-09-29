import pygame

# About position values in pygame
# -> https://stackoverflow.com/questions/62804292/how-to-set-the-position-of-an-image-in-pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, image_file, width, height , location, satamavahti=False):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.resized_image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.x, self.rect.y = location
        self.satamavahti = satamavahti

        if satamavahti == False:
            self.lahetetyt_apinat = 0
            self.apinat_perilla = 0

        if satamavahti == True:
            self.vastaanotetut_sanat = []


    def draw(self,screen):
        if self.satamavahti == False:
            self.apinaprosentti = 0
            if self.lahetetyt_apinat != 0:
                # desimaalien määrä https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
                self.apinaprosentti = round(((self.apinat_perilla / self.lahetetyt_apinat)*100),2)
            self.my_font = pygame.font.SysFont('Comic Sans MS', 17)
            self.text_surface = self.my_font.render(f"{self.apinat_perilla} / {self.lahetetyt_apinat} ({self.apinaprosentti} %)", False, (255, 0, 0))

            screen.blit(self.text_surface, (self.rect.left, self.rect.top-27))

        screen.blit(self.resized_image, self.rect)
        
    def vahdi(self, saapuneet_sanat):
        vahdi = True
        while vahdi == True:
            print("Lisätään sana listaan jos uusi")
            if len(saapuneet_sanat) > 9:
                print("Tässähän on hätä viesti!")

    