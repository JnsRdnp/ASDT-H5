import pygame
import sys
import threading
import time
from background import Background
from place import Place
from person import Person
from monkey import Monkey
from button import Button
from ship import Ship


# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ernest & Kernest Monkey Genocide")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

running = True

screen_needs_update = False

def update_screen():

    screen.fill(WHITE)
    screen.blit(Meri.resized_image, Meri.rect)
    screen.blit(Saari.resized_image, Saari.rect)
    screen.blit(Mantere.resized_image, Mantere.rect)
    screen.blit(Ernesti.resized_image, Ernesti.rect)
    screen.blit(Kernesti.resized_image, Kernesti.rect)

    ErnestiApina.draw(screen)
    ErnestiApinanappi.draw(screen)
    ErnestiApinanappi10.draw(screen)

    KernestiApina.draw(screen)
    KernestiApinanappi.draw(screen)
    KernestiApinanappi10.draw(screen)

    Ernesti.draw(screen)
    Kernesti.draw(screen)

    Pohteri.draw(screen, pohjoisen_sanat)
    PohteriVahdiNappi.draw(screen)
    PohterinLaiva.draw(screen)

    Eteteri.draw(screen, etelan_sanat)
    EteteriVahdiNappi.draw(screen)
    EteterinLaiva.draw(screen)

    # Dynaamisesti luotujen apinoiden piirtäminen
    for monkey in ErnestinApinat.values():
        monkey.draw(screen)

    for monkey in KernestinApinat.values():
        monkey.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Init sprites
Meri = Background(image_file = "./assets/meri.png", location = [0,0])

Saari = Place(image_file = "./assets/saari.png", width = 300,height = 400 ,location = [0,-5])
Mantere = Place(image_file = "./assets/mantere.png", width = 250, height = 400 , location = [WIDTH-230,10])

# Ernesti ja sen apinat
Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.top + 85])
ErnestiApina = Monkey(screen=screen, omistaja=Ernesti)
ErnestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+10,25,'Ernesti Apina')
ErnestiApinanappi10 = Button(BLACK, ErnestiApinanappi.button_rect.right+10,Meri.rect.bottom+10,25,'10x')

# Kernesti ja sen apinat
Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.bottom - 85])
KernestiApina = Monkey(screen=screen, omistaja=Kernesti)
KernestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+60,25,'Kernesti Apina')
KernestiApinanappi10 = Button(BLACK, KernestiApinanappi.button_rect.right+10,Meri.rect.bottom+60,25,'10x')

# Pohteri ja eteteri
Pohteri = Person(image_file = "./assets/pohteri.png", width = 60, height = 85, location = [Mantere.rect.centerx-45, Mantere.rect.top + 85], satamavahti=True)
PohteriVahdiNappi = Button(BLACK,Meri.rect.centerx+120,Meri.rect.bottom+10,25,'Pohteri vahdi')
PohteriVahdissa = False

Eteteri = Person(image_file = "./assets/eteteri.png", width = 60, height = 85, location = [Mantere.rect.centerx-50, Mantere.rect.bottom - 95], satamavahti=True)
EteteriVahdiNappi = Button(BLACK,Meri.rect.centerx+120, Meri.rect.bottom+60,25,'Eteteri vahdi')
EteteriVahdissa = False

# Laivat
PohterinLaiva = Ship(screen=screen, omistaja=Pohteri)
EteterinLaiva = Ship(screen=screen, omistaja=Eteteri)


# Mantereen ja saaren välimatka
valimatka = (Mantere.rect.left)-Saari.rect.right
hatasanoma_list = ["Tulee", "ärpeegeetä", "tuuksie", "helppaa", "huomen", "vai", "tänää", "v**tu", "mie", "kuolen"]

# Luodaan apinat dynaamiseesti niin että hätäsanoma sisällytetään olioon
def teach_10_monkeys(owner=Person, saapuneet_sanat=[]):
    monkeys = {}

    for i in range(10):
        sana = hatasanoma_list[i]  # Haetaan hatasanomasta yksi sana
        monkeys[f"monkey_{i+1}"] = Monkey(screen=screen , sana=sana, omistaja=owner, saapuneet_sanat=saapuneet_sanat)  # Luo apina ja talleta muide joukkoon

    return monkeys

pohjoisen_sanat  = []
etelan_sanat = []

ErnestinApinat = teach_10_monkeys(Ernesti, pohjoisen_sanat)
KernestinApinat = teach_10_monkeys(Kernesti, etelan_sanat)


def send_10_monkeys(monkeys,distance, vastaanottajavahdissa):

    # Luodaan uusi apinakatras saarelle (vanhat apinat syntyy saarelle takaisin)
    for monkey in monkeys.values():
        monkey.reset_monkey()

    for monkey in monkeys.values():
        # Lähetetään apinat jonossa uimaan että ne eivät ole läjässä
        threading.Thread(target=move_monkey, args=(monkey, distance, vastaanottajavahdissa)).start()
        time.sleep(0.65)


# Apinan liikuttelun aloitus eri funktiossa jotta voidaan hyödyntää threadingiä
def move_monkey(monkey, distance, vastaanottajavahdissa = False):
    monkey.reset_monkey()
    monkey.liikuMantereelle(valimatka=distance, vastaanottajavahdissa=vastaanottajavahdissa)

def pohteri_vahtii():
    print("Pohteri aloitti vahtimisen")
    vahdi = True

    global PohteriVahdissa
    PohteriVahdissa = True

    # Pidetään huolta että while looppi loppuu myös jos ohjelma lopetetaan
    global running


    # Lopettaa vahtimisen jos tulee 10 erilaista sanaa
    while vahdi == True and running == True:
        vahdi = Pohteri.vahdi(pohjoisen_sanat)
        if vahdi==False:
            PohterinLaiva.liikuSaarelle(valimatka=valimatka)

            #Iloitaan vain jos ollaan ensimmäisiä
            if Kernesti.iloitsee == False:
                Ernesti.iloitsee=True
        time.sleep(1)

def eteteri_vahtii():
    print("Eteteri aloitti vahtimisen")
    vahdi = True

    global EteteriVahdissa
    EteteriVahdissa = True

    # Pidetään huolta että while looppi loppuu myös jos ohjelma lopetetaan
    global running

    # Lopettaa vahtimisen jos tulee 10 erilaista sanaa tai ohjelma lopetetaan
    while vahdi == True and running == True:
        vahdi = Eteteri.vahdi(etelan_sanat)
        
        if vahdi==False:
            EteterinLaiva.liikuSaarelle(valimatka=valimatka)
            # Iloitaan vain jos ollaan ensimmäisiä
            if Ernesti.iloitsee == False:
                Kernesti.iloitsee=True

        time.sleep(1)
    


# Main game loop
def main():
    global running
    global EteteriVahdissa
    global PohteriVahdissa
    while running:
        for event in pygame.event.get():

            # ErnestiApina.liikuMantereelle(valimatka)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if ErnestiApinanappi.button_rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    threading.Thread(target=move_monkey, args=(ErnestiApina, valimatka)).start()
                
                if ErnestiApinanappi10.button_rect.collidepoint(mouse_pos):
                    threading.Thread(target=send_10_monkeys, args=(ErnestinApinat, valimatka, PohteriVahdissa)).start()


                if KernestiApinanappi10.button_rect.collidepoint(mouse_pos):
                    
                    threading.Thread(target=send_10_monkeys, args=(KernestinApinat, valimatka, EteteriVahdissa)).start()

                if KernestiApinanappi.button_rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    threading.Thread(target=move_monkey, args=(KernestiApina, valimatka)).start()

                if PohteriVahdiNappi.button_rect.collidepoint(mouse_pos):

                    threading.Thread(target=pohteri_vahtii).start()

                if EteteriVahdiNappi.button_rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    threading.Thread(target=eteteri_vahtii).start()


                

            if event.type == pygame.QUIT:
                
                running = False


        update_screen()
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
