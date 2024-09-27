import pygame
import sys
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

def update_screen():
    """Redraw everything on the screen."""
    screen.fill(WHITE)
    screen.blit(Meri.resized_image, Meri.rect)
    screen.blit(Saari.resized_image, Saari.rect)
    screen.blit(Mantere.resized_image, Mantere.rect)
    screen.blit(Ernesti.resized_image, Ernesti.rect)
    screen.blit(Kernesti.resized_image, Kernesti.rect)
    ErnestiApina.draw()
    ErnestiApinanappi.draw(screen)

    KernestiApina.draw()
    KernestiApinanappi.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)


# Init sprites
Meri = Background(image_file = "./assets/meri.png", location = [0,0])

Saari = Place(image_file = "./assets/saari.png", width = 300,height = 400 ,location = [0,-5])
Mantere = Place(image_file = "./assets/mantere.png", width = 200, height = 400 , location = [WIDTH-200,10])

Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.top + 85])
Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.bottom - 85])

ErnestiApina = Monkey(image_file = "./assets/apina.png", width = 50, height = 75, location = [Ernesti.rect.centerx+10, Ernesti.rect.top],
               screen=screen, update_screen_func=update_screen)

KernestiApina = Monkey(image_file = "./assets/apina.png", width = 50, height = 75, location = [Kernesti.rect.centerx+10, Kernesti.rect.top],
               screen=screen, update_screen_func=update_screen)

ErnestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+10,25,'Ernesti Apina')
KernestiApinanappi = Button(BLACK,Meri.rect.left+40,Meri.rect.bottom+60,25,'Kernesti Apina')

# Mantereen ja saaren välimatka
valimatka = Mantere.rect.left-Saari.rect.right 




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
                    ErnestiApina.liikuMantereelle(valimatka=valimatka)

                if KernestiApinanappi.button_rect.collidepoint(mouse_pos):
                    # prints current location of mouse
                    KernestiApina.liikuMantereelle(valimatka=valimatka)

            if event.type == pygame.QUIT:
                running = False


        update_screen()
        

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
