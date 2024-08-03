import pygame
import time
import math
import random
import sys

wScreen = 1200
hScreen = 500

width=50
height=20
vel=0.1
x=100
y=380
bullet_position_x= x+width/2
bullet_position_y= y+height/2
clock=pygame.time.Clock()

class ball(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)


    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)


def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (0,0,0),line[0], line[1])
    pygame.display.update()

def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


golfBall = ball(300,494,5,(255,255,255))

run = True
time = 0
power = 0
angle = 0
shoot = False


win = pygame.display.set_mode((wScreen,hScreen))
pygame.display.set_caption('Tank movement')

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:#left
        x-=vel
        bullet_position_x-=vel
    if keys[pygame.K_d]:#right
        x+=vel
        bullet_position_x+=vel
    if keys[pygame.K_ESCAPE]:
        run=False
    if x==350 or x>350:
        x=350
        bullet_position_x= x+width/2
    if x==0 or x<0:
        x=0
        bullet_position_x= x+width/2
    
    if keys[pygame.K_e]: 
        if not shoot:
                x = golfBall.x
                y = golfBall.y
                pos =pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                angle = findAngle(pos)
        


    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]
    
    win.fill((255,255,255))

    tank=pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    ground=pygame.draw.rect(win,(0,255,0),(0,400,1200,100))
    fence=pygame.draw.rect(win,(165,42,42),(400,340,20,60))
    bullet=pygame.draw.circle(win,(0,0,0),(bullet_position_x,bullet_position_y),1)
    

    pygame.display.flip()
    clock.tick(10)

pygame.quit()