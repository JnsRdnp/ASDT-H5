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

# Init sprites
Meri = Background(image_file = "./assets/meri.png", location = [0,0])

Saari = Place(image_file = "./assets/saari.png", width = 300,height = 400 ,location = [0,-5])
Mantere = Place(image_file = "./assets/mantere.png", width = 200, height = 400 , location = [WIDTH-200,10])

Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.top + 85])
Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, location = [Saari.rect.right-65, Saari.rect.bottom - 85])

Apina = Monkey(image_file = "./assets/apina.png", width = 50, height = 75, location = [Saari.rect.right-10, Saari.rect.bottom - 85])

Apinanappi = Button(BLACK,Meri.rect.left+20,Meri.rect.bottom+10,150,30,'Apina')

# Mantereen ja saaren välimatka
valimatka = Mantere.rect.left-Saari.rect.right 


# Set up the clock for controlling frame rate
clock = pygame.time.Clock()


# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():

            # Apina.liikuMantereelle(valimatka)

            if event.type == pygame.QUIT:
                running = False


        # Background setup
        screen.fill(WHITE)
        screen.blit(Meri.resized_image, Meri.rect)

        # Saari ja manner setup
        screen.blit(Saari.resized_image, Saari.rect)    
        screen.blit(Mantere.resized_image, Mantere.rect)    

        # Ihmiset setup
        screen.blit(Ernesti.resized_image, Ernesti.rect)
        screen.blit(Kernesti.resized_image, Kernesti.rect)

        # Apinat setup
        screen.blit(Apina.resized_image, Apina.rect)


        # Drawing code goes here
        Apinanappi.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
