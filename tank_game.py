import pygame
import math

pygame.init()
window_width = 1200
window_height = 500
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("tank game")
clock = pygame.time.Clock()
run = True
circle_size = 20

tank_speed=20
tank_height=20
tank_width=50

ground_level=window_height-window_height/8





dt=0
player_pos = pygame.Vector2(window_width/8,ground_level-tank_height)
class tank(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("C:/Users/super/OneDrive/Desktop/12ddt-python/PRoject/image/tank_sprite.png")
        self.rect = self.image.get_rect(center=(0,0))
        self.rect.topleft = (x,y)
        self.velocity = tank_speed


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("Sky blue")
    #draw the groud
    pygame.draw.rect(screen,(183,255,90),(0,ground_level,window_width,window_height/8))
    #draw a tank
    tank(player_pos.x,player_pos.y)
    screen.blit()

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        player_pos.x += dt * 100
    if key[pygame.K_a]:
        player_pos.x -= dt * 100

    if player_pos.x+tank_width>=window_width:
        player_pos.x=window_width-tank_width
    if player_pos.x<=0:
        player_pos.x=0
    

    dt = clock.tick(60)/1000
    pygame.display.flip()
