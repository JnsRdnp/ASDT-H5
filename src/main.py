import pygame
import sys
import threading
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
    # Päivitetään näyttöä jos kumpikaan ampina on liikkeessä näin ei tule päällikkeäisiä päivityksiä
     
    # if mainloop==False:
        
    #     global screen_needs_update
    #     print("Screen needs update ", screen_needs_update)
    #     if screen_needs_update:

    #         screen.fill(WHITE)
    #         screen.blit(Meri.resized_image, Meri.rect)
    #         screen.blit(Saari.resized_image, Saari.rect)
    #         screen.blit(Mantere.resized_image, Mantere.rect)
    #         screen.blit(Ernesti.resized_image, Ernesti.rect)
    #         screen.blit(Kernesti.resized_image, Kernesti.rect)
    #         ErnestiApina.draw()
    #         ErnestiApinanappi.draw(screen)

    #         KernestiApina.draw()
    #         KernestiApinanappi.draw(screen)

    #         # Update the display
    #         pygame.display.flip()
    #         screen_needs_update = False  # Reset flag after screen update
    
    # Jos funktiota on kutsuttu pääloopista niin suoritetaan normaalisti
    # else:

    screen.fill(WHITE)
    screen.blit(Meri.resized_image, Meri.rect)
    screen.blit(Saari.resized_image, Saari.rect)
    screen.blit(Mantere.resized_image, Mantere.rect)
    screen.blit(Ernesti.resized_image, Ernesti.rect)
    screen.blit(Kernesti.resized_image, Kernesti.rect)
    ErnestiApina.draw()
    ErnestiApinanappi.draw(screen)
    ErnestiApinanappi10.draw(screen)

    KernestiApina.draw()
    KernestiApinanappi.draw(screen)
    KernestiApinanappi10.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Init sprites
Meri = Background(image_file = "./assets/meri.png", location = [0,0])

Saari = Place(image_file = "./assets/saari.png", width = 300,height = 400 ,location = [0,-5])
Mantere = Place(image_file = "./assets/mantere.png", width = 200, height = 400 , location = [WIDTH-185,10])


Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.top + 85])
ErnestiApina = Monkey(image_file = "./assets/apina.png", width = 50, height = 75, location = [Ernesti.rect.centerx+10, Ernesti.rect.top],
               screen=screen, update_screen_func=update_screen)
ErnestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+10,25,'Ernesti Apina')
ErnestiApinanappi10 = Button(BLACK, ErnestiApinanappi.button_rect.right+10,Meri.rect.bottom+10,25,'10x')

Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.bottom - 85])
KernestiApina = Monkey(image_file = "./assets/apina.png", width = 50, height = 75, location = [Kernesti.rect.centerx+10, Kernesti.rect.top],
               screen=screen, update_screen_func=update_screen)
KernestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+60,25,'Kernesti Apina')
KernestiApinanappi10 = Button(BLACK, KernestiApinanappi.button_rect.right+10,Meri.rect.bottom+60,25,'10x')


# Mantereen ja saaren välimatka
valimatka = Mantere.rect.left-Saari.rect.right 

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


    
