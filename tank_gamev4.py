import pygame
import math
import random

pygame.init()
pygame.font.init()

Wscreen = 1200
Hscreen = 600
win = pygame.display.set_mode((Wscreen,Hscreen))
text_font = pygame.font.Font("Tank game\press-start-2p-font\PressStart2P-vaV7.ttf",30)
tutorial_font = pygame.font.Font("Tank game\press-start-2p-font\PressStart2P-vaV7.ttf",25)
Menu_font = pygame.font.Font("Tank game/press-start-2p-font/PressStart2P-vaV7.ttf", 50)
clock = pygame.time.Clock()
BUTTON_WIDTH = 500
BUTTON_HEIGHT = 100
WHITE = (255, 255, 255)
BLACK = (0,0, 0)
button_image = pygame.image.load('Tank game/sprites/button.png')
button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
cloud_1_image = pygame.image.load('Tank game/sprites/cloud_1.png')
cloud_2_image = pygame.image.load('Tank game/sprites/cloud_2.png')
cloud_1_image=pygame.transform.scale(cloud_1_image,(Wscreen,Hscreen))
cloud_2_image=pygame.transform.scale(cloud_2_image,(Wscreen,Hscreen))

        
class Button:
        def __init__(self, x, y, image, text):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.text = text
            self.text_color = WHITE
            self.text_surf = Menu_font.render(self.text, True, self.text_color)
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)

        def draw(self, screen):
            self.text_surf = Menu_font.render(self.text, True, self.text_color)
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
            screen.blit(self.image, self.rect.topleft)
            screen.blit(self.text_surf, self.text_rect.topleft)

        def is_hovered(self, pos):
            return self.rect.collidepoint(pos)       



def draw_text(text, font, color, x , y):
    text_O = font.render(text,True,color)
    text_rect = text_O.get_rect()
    text_rect.center=(x,y)
    win.blit(text_O,text_rect)


def get_high_score():
    with open("Tank game/highscore.txt","r") as file:
        return int(file.read())

        
        

def tutorial_screen():
    pygame.display.set_caption('Tutorial')
    understand_button = Button(Wscreen / 2 - BUTTON_WIDTH / 2, Hscreen - 200 , button_image, 'OK!')
    run = True
    def redrawscreen():
        win.fill("sky blue")
        draw_text('''Up arrow to increse power''',tutorial_font, (0,0,0), Wscreen/2,40)
        draw_text('''Down arrow to decrese power''',tutorial_font, (0,0,0), Wscreen/2,80)
        draw_text('''Right arrow to decrese angle''',tutorial_font, (0,0,0), Wscreen/2,120)
        draw_text('''Left arrow to increse angle''',tutorial_font, (0,0,0), Wscreen/2,160)
        draw_text('''Press A to go left''',tutorial_font, (0,0,0), Wscreen/2,200)
        draw_text('''Press D to go right''',tutorial_font, (0,0,0), Wscreen/2, 240)
        draw_text('''Press E to shoot''',tutorial_font, (0,0,0), Wscreen/2,280)
        draw_text('''Wipe the filthy terrorist''',tutorial_font, (0,0,0),Wscreen/2,320)
        draw_text('''OFF THE FACE OF THIS EARTH!!!!!!''',tutorial_font, (0,0,0),Wscreen/2,360)
        understand_button.draw(win)
        pygame.display.update()
        
    while run:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if understand_button.is_hovered(event.pos):
                    win.fill("black")
                    run = False
                    

        # Change text color on hover
        if understand_button.is_hovered(pygame.mouse.get_pos()):
            understand_button.text_color = WHITE
            pygame.display.update()
        else:
            understand_button.text_color = BLACK
            pygame.display.update()
        redrawscreen()
        
    
        






def game():
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()

    tank_width = 50
    tank_height = 20

    vel = 1

    x = 0
    y = 0
    angle = 0
    power = 0
    time = 0
    shoot = False
    angle_limit = math.pi/2
    angle_movement_vercinity = math.pi/180
    gravity = -5.5
    ground_level=30
    score = 0
    combo = 0
    



    fence = pygame.Rect(Wscreen/5,Hscreen-ground_level-40,20,40)
    ground_image = pygame.image.load("Tank game/sprites/GRASS.png")
    ground_image = pygame.transform.scale(ground_image , (Wscreen,ground_level))


    class tank():
        def __init__(self, x, y, barrel_image_path, tank_body_path):
            self.body_width = 50
            self.body_height = 20
            self.body_color = (0,255,0)

            self.x = x
            self.y = y
            
            self.barrel_image = pygame.image.load(barrel_image_path)
            self.tank_body_image = pygame.image.load(tank_body_path)
            self.barrel_angle = 0            
            self.body = pygame.Rect(x, y, self.body_width, self.body_height)
            self.barrel_rect = self.barrel_image.get_rect(center=self.body.center)
            self.body_rect = self.tank_body_image.get_rect(topleft=(self.x,self.y))

        def rotate_barrel(self, angle_change):
            self.barrel_angle += angle_change
            self.barrel_image = pygame.transform.rotate(pygame.image.load('Tank game/sprites/Barrel.png'), self.barrel_angle)
            self.barrel_rect = self.barrel_image.get_rect(center=self.body.center)
        
        def draw(self, win):
            # Draw the barrel
            win.blit(self.barrel_image, (self.barrel_rect.topleft[0],self.barrel_rect.topleft[1]-3))
            # Draw the tank body
            win.blit(self.tank_body_image,(self.body_rect.topleft[0],self.body_rect.topleft[1]))
            
        
        def move(self, vel):
            self.body.x += vel
            self.barrel_rect.x += vel
            self.body_rect.x += vel
                                
            
    class buldings(object):
        def __init__(self,y,image_path):
            self.x = random.randint(Wscreen/5+20,1200-21)
            self.y = y
            self.image_path = image_path
            self.city_image = pygame.image.load(image_path)
            self.rect = self.city_image.get_rect(topleft=(self.x,self.y))
        def change_position(self):
            self.x = random.randint(Wscreen/5+20,1200-128)
        def draw(self,win):
            win.blit(self.city_image,(self.x,self.rect.topleft[1]+3))
        def when_hit(self):
            self.city_image = pygame.image.load("Tank game\sprites\city_explosion.png")
            redrawwindow()
            pygame.time.delay(400)
            self.city_image = pygame.image.load(self.image_path)
            redrawwindow()
        

    class cloud():
        def __init__(self,cloud_1_path,cloud_2_path):
            self.cloud_1=pygame.image.load(cloud_1_path)
            self.cloud_2=pygame.image.load(cloud_2_path)
            self.cloud_1=pygame.transform.scale(self.cloud_1,(1000,200))
            self.cloud_2=pygame.transform.scale(self.cloud_2,(1000,200))
            self.cloud_1_x = 0
            self.cloud_2_x = -1200
        def draw(self):
            win.blit(self.cloud_1,(self.cloud_1_x,0))
            win.blit(self.cloud_2,(self.cloud_2_x,0))
        def move_cloud(self):
            self.cloud_1_x+=1
            self.cloud_2_x+=1
            if self.cloud_1_x >=1200:
                self.cloud_1_x = -1200
            if self.cloud_2_x >=1200:
                self.cloud_2_x = -1200



        
        
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
            distY = (vely * time) + ((gravity * (time ** 2)) / 2)

            newx = round(distX + startx)
            newy = round(starty - distY)


            return (newx, newy)

    clouds=cloud("Tank game\sprites\cloud_1.png","Tank game\sprites\cloud_2.png")
    def redrawwindow():  
        win.fill((100, 173, 217))
        clouds.draw()
        win.blit(ground_image, (0,Hscreen-ground_level))
        normal_bullet.draw(win)
        player.draw(win)
        building.draw(win)
        pygame.draw.rect(win, (165, 42, 42), fence) #fence
        draw_text(f'''angle: {round(angle*(180/math.pi))} ''', text_font, (0,0,0), Wscreen/6,20)
        draw_text(f"power: {round(power)} m/s", text_font, (0,0,0), Wscreen/6,50)
        draw_text(f"score: {score}",text_font,(0,0,0),Wscreen/2,50)
        draw_text(f'''Time left: {round(timer_left)} ''', text_font, (0,0,0), Wscreen/2,20)
        draw_text(f'''Combo {combo} ''', text_font, (0,0,0), Wscreen/2,80)
        clouds.move_cloud()
        pygame.display.update()

    def countdown():
        win.fill(BLACK)
        draw_text(f'''3''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)
        draw_text(f'''2''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)
        draw_text(f'''1''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)
        draw_text(f'''SHOOT!''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(500)


    def game_over():
        win.fill(BLACK)
        draw_text(f'''TIME!''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)
        draw_text(f'''GAME OVER''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)
        draw_text(f'''Your score is {score}''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.display.update()
        pygame.time.delay(4000)
        win.fill(BLACK)
        draw_text(f'''Thank you for playing!''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
        pygame.time.delay(1000)
        if get_high_score()<score:
            win.fill(BLACK)
            draw_text(f'''You got a new High Score!!!''', text_font, (255,255,255), Wscreen/2,Hscreen/2)
            pygame.time.delay(1000)
        pygame.display.update()
        

    def high_score_change():
        with open("Tank game/highscore.txt","r") as file:
            if int(file.read())<score:
                with open("Tank game/highscore.txt","w") as file:
                    file.write(str(score))


    


    
    timer_left = 60
    player = tank(Wscreen/8,Hscreen-20-ground_level,"Tank game/sprites/Barrel.png","Tank game/sprites/Tank_body.png")
    normal_bullet = bullet(player.body.x+tank_width/2 , player.body.y+tank_height/2 ,2,(0,0,0))
    building = buldings(Hscreen-ground_level-66,"Tank game\sprites\city.png")
    run = True
    countdown()
    while run:

        
        clock.tick(120)
        redrawwindow()

        if shoot == True:
            time += 0.1
            position = bullet.path(x,y,power,angle,time)
            normal_bullet.x = position[0] #position is a list, like x,y, like [x,y], so im getting the x position in the list with 0
            normal_bullet.y = position[1]
            if normal_bullet.y >= Hscreen - normal_bullet.radius-ground_level:               
                shoot = False                           
                normal_bullet.x = player.body.x+tank_width/2
                normal_bullet.y = player.body.y+tank_height/2
                combo = 0
            elif normal_bullet.x+normal_bullet.radius >= Wscreen/5 and normal_bullet.y+normal_bullet.radius >= Hscreen-ground_level-40 and normal_bullet.x<=Wscreen/5+20:
                shoot = False
                normal_bullet.x = player.body.x+tank_width/2
                normal_bullet.y = player.body.y+tank_height/2     
                combo = 0    
            elif normal_bullet.x+normal_bullet.radius >= building.x and normal_bullet.x<=building.x+128 and normal_bullet.y+normal_bullet.radius >= Hscreen-ground_level-69:               
                shoot = False       
                normal_bullet.x = player.body.x+tank_width/2
                normal_bullet.y = player.body.y+tank_height/2
                building.when_hit()
                building.change_position()
                combo += 1
                score += 100*combo
                

                
        
        
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()

        if key[pygame.K_a] and player.body.x > 0:
            player.move(-vel)
            normal_bullet.x -= vel
        if key[pygame.K_d] and player.body.x < Wscreen/5-50:
            player.move(vel)
            normal_bullet.x += vel
        

        if key[pygame.K_e]:
            if shoot == False:
                shoot = True
                x = normal_bullet.x
                y = normal_bullet.y
                time = 0


        if key[pygame.K_LEFT] and not shoot:
            if angle >=0:
                angle += angle_movement_vercinity
                player.rotate_barrel(angle_movement_vercinity*(180/math.pi))
                if player.barrel_angle >= 90:
                    player.barrel_angle = 90
                if angle > angle_limit:
                    angle = angle_limit
                
        if key[pygame.K_RIGHT] and not shoot:
            if angle <= angle_limit:
                angle-= angle_movement_vercinity
                player.rotate_barrel(-(angle_movement_vercinity*(180/math.pi)))
                if angle <=0:
                    angle = 0
                if player.barrel_angle <= 0:
                    player.barrel_angle = 0
        if key[pygame.K_UP] and not shoot:
            if power >=0:
                power += 0.3                
                if power >100:
                    power = 100
        if key[pygame.K_DOWN] and not shoot:
            if power <= 100:
                power-=0.3              
                if power <=0:
                    power = 0
        timer_left-=1/120
        if timer_left <= 0:
            run = False
    game_over()
    high_score_change()



        
    



def menu():
    
    logo_image = pygame.image.load("Tank game/sprites/Logo.png")
    logo_image = pygame.transform.scale(logo_image,(600,400))
    
    # Set up the display
    screen = pygame.display.set_mode((Wscreen, Hscreen))
    pygame.display.set_caption('Menu')

    # Font settings
    

    # Button class
    class logo:
        def __init__(self,x,y,image):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.topleft=(x,y)
        def draw(self, screen):
            screen.blit(self.image, self.rect.topleft)


    # Create a button instance
    start_button = Button(Wscreen / 2 - BUTTON_WIDTH / 2, Hscreen / 2-60 , button_image, 'Start')
    quit_button=Button(Wscreen / 2 - BUTTON_WIDTH / 2, Hscreen -200 , button_image, 'Quit')
    Logo=logo(Wscreen / 2 -300, Hscreen / 2 - 380 ,logo_image)
    def redrawscreen():
        screen.fill("sky blue")
        start_button.draw(screen)
        draw_text(f"High Score: {get_high_score()}",text_font,(0,0,0),Wscreen/2,Hscreen/2+65)
        quit_button.draw(screen)
        Logo.draw(screen)
        pygame.display.update()

    # Main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_hovered(event.pos):
                    win.fill("black")
                    tutorial_screen()
                    win.fill("black")
                    game()
                if quit_button.is_hovered(event.pos):
                    run=False

        # Change text color on hover
        try:
            if start_button.is_hovered(pygame.mouse.get_pos()):
                start_button.text_color = WHITE
            else:
                start_button.text_color = BLACK

            if quit_button.is_hovered(pygame.mouse.get_pos()):
                quit_button.text_color = WHITE
            else:
                quit_button.text_color = BLACK
        except pygame.error:
            pass
        redrawscreen()
        

menu()
