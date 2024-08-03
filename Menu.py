import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 500
BUTTON_HEIGHT = 100
WHITE = (255, 255, 255)
RED = (0,0, 0)

# Load button image
button_image = pygame.image.load('sprites/button.png')
button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
logo_image=pygame.image.load("sprites/Logo.png")
logo_image=pygame.transform.scale(logo_image,(600,400))
 
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Menu Example')

# Font settings
font = pygame.font.Font("press-start-2p-font\PressStart2P-vaV7.ttf", 50)

# Button class
class logo:
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


	
class Button:
    def __init__(self, x, y, image, text):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.text_color = WHITE
        self.text_surf = font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        self.text_surf = font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.text_surf, self.text_rect.topleft)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

# Create a button instance
button = Button(SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2-60 , button_image, 'Start')
Logo=logo(SCREEN_WIDTH / 2 -300, SCREEN_HEIGHT / 2 - 380 ,logo_image)
def redrawscreen():
    screen.fill("sky blue")
    button.draw(screen)
    Logo.draw(screen)
    pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_hovered(event.pos):
                print('Button clicked!')

    # Change text color on hover
    if button.is_hovered(pygame.mouse.get_pos()):
        button.text_color = RED
    else:
        button.text_color = WHITE
    redrawscreen()

    
    

pygame.quit()
sys.exit()
