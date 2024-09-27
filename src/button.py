import pygame

# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame

class Button():

    pygame.font.init()

    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        

        self.button_rect = pygame.Rect(self.x,self.y,self.width,self.height)

        # Numeron pyöristys https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number
        self.my_font = pygame.font.SysFont('Comic Sans MS', int(self.button_rect.height/1.5))

        # self.text_width, self.text_height = self.font.size(text)

    def draw(self,screen):
        text_surface = self.my_font.render(self.text, False, (255, 255, 255))
        
        pygame.draw.rect(screen, self.color, self.button_rect,0)
        screen.blit(text_surface, (self.button_rect.left+self.button_rect.width/4, self.button_rect.top))