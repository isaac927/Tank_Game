import pygame
import math
import random

pygame.init()
pygame.font.init()

Wscreen = 1200
Hscreen = 500
win = pygame.display.set_mode((Wscreen,Hscreen))
text_font = pygame.font.Font("press-start-2p-font\PressStart2P-vaV7.ttf",30)
clock = pygame.time.Clock()


        
        
        
        







def game():
    pygame.display.set_caption('Game')
    text_font = pygame.font.Font("press-start-2p-font\PressStart2P-vaV7.ttf",20)
    clock = pygame.time.Clock()

    tank_width = 50
    tank_height = 20

    vel = 2

    x = 0
    y = 0
    angle = 0
    power = 0
    time = 0
    shoot = False
    angle_limit = math.pi/2
    angle_movement_vercinity = math.pi/200
    gravity = -2
    ground_level=30


    fence = pygame.Rect(Wscreen/5,Hscreen-ground_level-50,20,50)
    ground=pygame.Rect(0, Hscreen-ground_level, Wscreen, 100)


    class tank():
        def __init__(self, x , y,barrel_image):
            self.x = x
            self.y = y
            self.barrel_image = barrel_image
        def draw(self, win):
            pygame.draw.rect(win, (126,255,0), pygame.Rect(player.x, player.y, tank_width,tank_height))
            win.blit(self.barrel_image,(self.x,self.y-20))


    class bullet(object):
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
        
        def draw(self, win):
            pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        
        def path(startx,starty,power,angle,time):
            velx = math.cos(angle) * power
            vely = math.sin(angle) * power

            distX = velx * time
            distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

            newx = round(distX + startx)
            newy = round(starty - distY)


            return (newx, newy)

    class explosion():
        def __init__(self, x, y ,radius ,color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
        def draw(self, win):
            pygame.draw.circle(win, (255,165,0), (self.x,self.y), self.radius)

    def redrawwindow():
        win.fill((135, 206, 235))
        pygame.draw.rect(win , (0,255,0), ground)
        normal_bullet.draw(win)
        player.draw(win)
        pygame.draw.rect(win, (165, 42, 42), fence) #fence
        draw_text(f'''angle: {round(angle*(180/math.pi))} ''', text_font, (0,0,0), 0,0)
        draw_text(f"power: {power} m/s", text_font, (0,0,0), 0,30)
        pygame.display.update()

    def explosion_animation():
        explosion_circle = explosion(normal_bullet.x, normal_bullet.y,30, (255,165,0))
        explosion_circle.draw(win)
        pygame.display.update()

    def draw_text(text, font, color, x , y):
        img = font.render(text,True,color)
        win.blit(img, (x,y))
    barrel_image=pygame.image.load("sprites/Barrel.png")
    barrel_image=pygame.transform.scale(barrel_image,(tank_width,tank_height+20))
    player = tank(Wscreen/8,Hscreen-20-ground_level,barrel_image)
    normal_bullet = bullet(player.x+tank_width/2 , player.y+tank_height/2 ,2,(0,0,0))
    run = True
    while run:
        redrawwindow()
        clock.tick(120)


        if shoot == True:
            time += 0.1
            position = bullet.path(x,y,power,angle,time)
            normal_bullet.x = position[0] #position is a list, like x,y, like [x,y], so im getting the x position in the list with 0
            normal_bullet.y = position[1]
            if normal_bullet.y >= Hscreen - normal_bullet.radius-ground_level:
                shoot = False
                explosion_animation()
                pygame.time.delay(200)
                normal_bullet.x = player.x+tank_width/2
                normal_bullet.y = player.y+tank_height/2       
            elif normal_bullet.x+normal_bullet.radius >= Wscreen/5 and normal_bullet.y+normal_bullet.radius >= Hscreen-ground_level-50 and normal_bullet.x<=Wscreen/5+20:
                shoot = False
                explosion_animation()
                pygame.time.delay(200)
                normal_bullet.x = player.x+tank_width/2
                normal_bullet.y = player.y+tank_height/2
            else:
                pass
        
                
                


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x > 0:
            player.x -= vel
            normal_bullet.x -= vel
        if key[pygame.K_d] and player.x < Wscreen/5-50:
            player.x += vel
            normal_bullet.x += vel
        if key[pygame.K_e]:
            if shoot == False:
                shoot = True
                x = normal_bullet.x
                y = normal_bullet.y
                time = 0
        if key[pygame.K_RIGHT] and not shoot:
            if angle >=0:
                angle += angle_movement_vercinity
                if angle > angle_limit:
                    angle = angle_limit
        if key[pygame.K_LEFT] and not shoot:
            if angle <= angle_limit:
                angle-= angle_movement_vercinity
                if angle <=0:
                    angle = 0
        if key[pygame.K_UP] and not shoot:
            if power >=0:
                power += 1
                barrel_image=pygame.transform.rotate(barrel_image,1)
                if power >100:
                    power = 100
        if key[pygame.K_DOWN] and not shoot:
            if power <= 100:
                power-=1
                if power <=0:
                    power = 0
    



def menu():
    BUTTON_WIDTH = 500
    BUTTON_HEIGHT = 100
    WHITE = (255, 255, 255)
    BLACK = (0,0, 0)

    # Load button image
    button_image = pygame.image.load('sprites/button.png')
    button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
    logo_image=pygame.image.load("sprites/Logo.png")
    logo_image=pygame.transform.scale(logo_image,(600,400))
    
    # Set up the display
    screen = pygame.display.set_mode((Wscreen, Hscreen))
    pygame.display.set_caption('Menu')

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
    start_button = Button(Wscreen / 2 - BUTTON_WIDTH / 2, Hscreen / 2-60 , button_image, 'Start')
    quit_button=Button(Wscreen / 2 - BUTTON_WIDTH / 2, Hscreen -200 , button_image, 'Quit')
    Logo=logo(Wscreen / 2 -300, Hscreen / 2 - 380 ,logo_image)
    def redrawscreen():
        screen.fill("sky blue")
        start_button.draw(screen)
        quit_button.draw(screen)
        Logo.draw(screen)
        pygame.display.update()

    # Main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_hovered(event.pos):
                    win.fill("black")
                    game()
                if quit_button.is_hovered(event.pos):
                    run=False

        # Change text color on hover
        if start_button.is_hovered(pygame.mouse.get_pos()):
            start_button.text_color = WHITE
        else:
            start_button.text_color = BLACK

        if quit_button.is_hovered(pygame.mouse.get_pos()):
            quit_button.text_color = WHITE
        else:
            quit_button.text_color = BLACK
        redrawscreen()
        

menu()