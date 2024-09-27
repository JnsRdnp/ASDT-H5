import pygame
import sys
from background import Background
from place import Place

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


# Init sprites
Meri = Background("./assets/meri.png", [0,0])
Saari = Place("./assets/saari.png", 200, 400 ,[0,-5])
Mantere = Place("./assets/mantere.png", 200, 400 ,[WIDTH-200,10])


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

        # Drawing code goes here


        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


    
