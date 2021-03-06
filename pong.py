import pygame
import time
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280,720))
done = False
#set initial variables
p1_x,p1_y=30,30
p2_x,p2_y=(screen.get_width()-60),30
ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
slope_x,slope_y=2,2
#set constants
paddle_width = screen.get_width()/64
paddle_height = screen.get_height()/3.6
#define Paddle class
class Paddle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_height))
        self.rect=pygame.Rect(self.x,self.y,paddle_width,paddle_height)
    def draw(self):
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_height))
        self.rect=pygame.Rect(self.x,self.y,paddle_width,paddle_height)
    def up(self):
        if self.y>0:
            self.y-=3
    def down(self):
        if self.y<screen.get_height()-200: 
            self.y+=3
#define ball class
class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.slope_x=slope_x
        self.slope_y=slope_y
        self.ball=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_width))
        self.rect = pygame.Rect(self.x,self.y,paddle_width,paddle_width)
    def draw(self):
        #make ball movement
        self.x+=self.slope_x
        self.y+=self.slope_y
        if self.y <= 0 or self.y >= (screen.get_height()):
            self.slope_y*=-1
        if self.x <= 0:
            self.slope_x*=-1
            #p2_score+=1
            self.x,self.y=((screen.get_width())/2),((screen.get_height())/2)
            time.sleep(1)
        if self.x >= (screen.get_width()):
            self.slope_x*=-1
            #p1_score+=1
            self.x,self.y=((screen.get_width())/2),((screen.get_height())/2)
            time.sleep(1)
        #collision
        if self.rect.colliderect(p1.rect) or self.rect.colliderect(p2.rect):
            self.col()
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_width))
        self.rect = pygame.Rect(self.x,self.y,paddle_width,paddle_width)
    def col(self):
        self.slope_x*=-1
        if self.slope_y>0:
            self.slope_y=random.randint(1,3) * -1
        else:
            self.slope_y=random.randint(1,3)
        self.x+=(self.slope_x*3)
        self.y+=self.slope_y


#set initial conditions
p1_score,p2_score=0,0
p1=Paddle(p1_x,p1_y)
p2=Paddle(p2_x,p2_y)
ball=Ball(ball_x,ball_y)

#main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    
    #controls
    #p1
    if pressed[pygame.K_w]:
        p1.up()
    if pressed[pygame.K_s]:
        p1.down()
    #p2
    if pressed[pygame.K_UP]:
        p2.up()
    if pressed[pygame.K_DOWN]:
        p2.down()

    #make players and ball
    screen.fill((0,0,0))
    score = myfont.render(str(p1_score)+" "+str(p2_score), True, (255,255,255))
    screen.blit(score, ((screen.get_width()/2)-20,0))
    p1.draw()
    p2.draw()
    ball.draw()

    pygame.display.flip()