import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Example")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Tank:
    def __init__(self, x, y, barrel_image_path):
        self.body_width = 50
        self.body_height = 20
        self.body_color = GREEN

        self.barrel_image = pygame.image.load(barrel_image_path)
        self.barrel_angle = 0
        
        self.body = pygame.Rect(x, y, self.body_width, self.body_height)
        self.barrel_rect = self.barrel_image.get_rect(center=self.body.center)

    def rotate_barrel(self, angle_change):
        self.barrel_angle += angle_change
        self.barrel_angle %= 360  # Keep angle in [0, 360)
        self.barrel_image = pygame.transform.rotate(pygame.image.load('sprites/Barrel.png'), self.barrel_angle)
        self.barrel_rect = self.barrel_image.get_rect(center=self.body.center)

    def move(self, dx):
        self.body.x += dx
        self.barrel_rect.x += dx

    def draw(self, screen):
        # Draw the tank body
        pygame.draw.rect(screen, self.body_color, self.body)
        # Draw the barrel
        screen.blit(self.barrel_image, self.barrel_rect.topleft)

def main():
    tank = Tank(screen_width // 2, screen_height // 2, 'sprites/Barrel.png')  # Replace 'barrel.png' with your barrel image path
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle input for moving the tank and rotating the barrel
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tank.rotate_barrel(2)  # Rotate barrel left
        if keys[pygame.K_RIGHT]:
            tank.rotate_barrel(-2)  # Rotate barrel right
        if keys[pygame.K_a]:
            tank.move(-5)  # Move left
        if keys[pygame.K_d]:
            tank.move(5)  # Move right

        # Clear the screen
        screen.fill(WHITE)

        # Draw the tank
        tank.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
