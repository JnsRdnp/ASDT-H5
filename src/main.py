import pygame
import sys
from background import Background
from place import Place
from person import Person

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


# Init sprites
Meri = Background(image_file = "./assets/meri.png", location = [0,0])

Saari = Place(image_file = "./assets/saari.png", width = 200,height = 400 ,location = [0,-5])
Mantere = Place(image_file = "./assets/mantere.png", width = 200, height = 400 , location = [WIDTH-200,10])

Ernesti = Person(image_file = "./assets/erne.png", width = 50, height = 75, initial_x = Saari.rect.right-50, initial_y = Saari.rect.top + 85)
Kernesti = Person(image_file = "./assets/kerne.png", width = 50, height = 75, initial_x = Saari.rect.right-50, initial_y = Saari.rect.bottom - 85)


# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here

        # Background setup
        screen.fill(WHITE)
        screen.blit(Meri.resized_image, Meri.rect)

        # Saari ja manner setup
        screen.blit(Saari.resized_image, Saari.rect)    
        screen.blit(Mantere.resized_image, Mantere.rect)    

        # Ihmiset setup
        screen.blit(Ernesti.resized_image, Ernesti.rect)
        screen.blit(Kernesti.resized_image, Kernesti.rect)

        # Drawing code goes here


        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
