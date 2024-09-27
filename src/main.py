import pygame
import sys
from background import Background

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

Meri = Background("./assets/meri.png", [0,0])


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

        # Fill the screen with a background color
        screen.fill(WHITE)
        screen.blit(Meri.image, Meri.rect)

        # Drawing code goes here
        

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()