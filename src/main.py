import pygame
import sys
import threading
import time
from background import Background
from place import Place
from person import Person
from monkey import Monkey
from button import Button


# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

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

    # Muiden luotujen apinoiden piirtäminen
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
Mantere = Place(image_file = "./assets/mantere.png", width = 200, height = 400 , location = [WIDTH-185,10])

# Ernesti ja sen apinat
Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.top + 85])

ErnestinApinoidenStart  = [Ernesti.rect.centerx+10, Ernesti.rect.top]
ErnestiApina = Monkey(location = ErnestinApinoidenStart, screen=screen)

ErnestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+10,25,'Ernesti Apina')
ErnestiApinanappi10 = Button(BLACK, ErnestiApinanappi.button_rect.right+10,Meri.rect.bottom+10,25,'10x')



# Kernesti ja sen apinat
Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.bottom - 85])

KernestinApinoidenStart  = [Kernesti.rect.centerx+10, Kernesti.rect.top]
KernestiApina = Monkey(location=KernestinApinoidenStart, screen=screen)
 
KernestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+60,25,'Kernesti Apina')
KernestiApinanappi10 = Button(BLACK, KernestiApinanappi.button_rect.right+10,Meri.rect.bottom+60,25,'10x')


# Mantereen ja saaren välimatka
valimatka = (Mantere.rect.left)-Saari.rect.right
hatasanoma_list = ["Tulee", "ärpeegeetä", "tuuksie", "helppaa", "huomen", "vai", "tänää", "v**tu", "mie", "kuolen"]

# Luodaan apinat dynaamiseesti niin että niiden nimi on hätäsanoma ja ne osaavat sen myös
def teach_10_monkeys(start=[]):
    monkeys = {}

    for i in range(10):
        sana = hatasanoma_list[i]  # Haetaan hatasanomasta yksi sana
        monkeys[f"monkey_{i+1}"] = Monkey(location=start, screen=screen ,sana=sana)  # Luo apina ja talleta muide joukkoon

    return monkeys


ErnestinApinat = teach_10_monkeys(ErnestinApinoidenStart)
KernestinApinat = teach_10_monkeys(KernestinApinoidenStart)


def send_10_monkeys(monkeys,distance):
    for monkey in monkeys.values():
        # Lähetetään apinat jonossa matkaan että ne eivät ole läjässä
        threading.Thread(target=move_monkey, args=(monkey, distance)).start()
        time.sleep(0.65)


# Apinan liikuttelun aloitus eri funktiossa jotta voidaan hyödyntää threadingiä
def move_monkey(monkey, distance):
    monkey.liikuMantereelle(valimatka=distance)


# Main game loop
def main():
    running = True
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
                    
                    threading.Thread(target=send_10_monkeys, args=(ErnestinApinat, valimatka)).start()


                if KernestiApinanappi10.button_rect.collidepoint(mouse_pos):
                    
                    threading.Thread(target=send_10_monkeys, args=(KernestinApinat, valimatka)).start()

                    
                if KernestiApinanappi.button_rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    threading.Thread(target=move_monkey, args=(KernestiApina, valimatka)).start()

                

            if event.type == pygame.QUIT:
                running = False


        update_screen()
        

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
