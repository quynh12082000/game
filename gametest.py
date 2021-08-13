from random import randint   
import pygame
from pygame.mixer import *
pygame.init()
screen = pygame.display.set_mode((700,400))
pygame.display.set_caption('duy mat l')
clock=pygame.time.Clock()
white=(255,255,255)
green=(0,255,0)
RED=(255,0,0)
oro=(153,0,76)
hack123=False
hack1=False
game_over=False
x_bird = 50
y_bird = 200
tube_width= 50
tube1_height=randint(250,400)
tube2_height=randint(250,400)
tube3_height=randint(250,400)
d_2tube=150
score=-3
hack12=False
font=pygame.font.SysFont('san',50)
font1=pygame.font.SysFont('san',35)
tube_velocity=3
x_colum=1000
x_colum1=1111
x_colum2=1222
x_colum=randint(300,700)
y_colum=randint(0,400)
x_colum1=randint(300,700)
y_colum1=randint(0,400)
x_colum2=randint(300,700)
y_colum2=randint(0,400)
tubez=True
tube1_x=400
BACKGROUND = pygame.image.load('img/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(700,400))
BIRDIMG = pygame.image.load('img/bird.png')
BIRDIMG = pygame.transform.scale(BIRDIMG,(50,50))
tube_img = pygame.image.load('img/tube.png')
tube_dow_img = pygame.image.load('img/tube_op.png')
tube1_pass=False
tube2_pass=False
tube3_pass=False
tubeq=True
pausing=False
runing = True
while runing:
    clock.tick(60)   
    screen.fill(white)
    screen.blit(BACKGROUND,(0,0))
    score_txt=font.render("score: "+str(score),True,white)
    score_txt=screen.blit(score_txt,(130,30))
    if x_bird and y_bird != x_colum and y_colum and tube1_pass==False:
        score+=1
        tube1_pass=True
    if x_bird and y_bird != x_colum1 and y_colum1 and tube2_pass==False:
        score+=1
        tube2_pass=True
    if x_bird and y_bird != x_colum2 and y_colum2 and tube3_pass==False:
        score+=1
        tube3_pass=True
    # di chuyen
    x_colum-=tube_velocity
    x_colum1-=tube_velocity
    x_colum2-=tube_velocity
    # x_colum3-=tube_velocity
    #tao cac thien thach moi
    
    if x_colum<-x_colum1:
        x_colum =700
        tube1_pass=False
    if x_colum2<-x_colum:
        x_colum2 =700
        tube2_pass=False
    if x_colum1<-x_colum2:
        x_colum1 =700
        tube3_pass=False
    if y_colum1<-y_colum2:
        y_colum1 =700
        tube2_pass=False
    if y_colum<-y_colum1:
        y_colum =700
        tube1_pass=False
    # if y_colum2<-y_colum:
    #     y_colum2 =700

    #ve may bay
    bird=screen.blit(BIRDIMG,(x_bird,y_bird))
    #ve thien thach
    if tubez:
        tube1_img = pygame.transform.scale(tube_img,(50,50))
        tube1=screen.blit(tube1_img,(x_colum,y_colum))
        
        tube2_img = pygame.transform.scale(tube_img,(50,50))
        tube2=screen.blit(tube2_img,(x_colum1,y_colum1))

        tube3_img = pygame.transform.scale(tube_dow_img,(50,50))
        tube3=screen.blit(tube3_img,(x_colum2,y_colum2))
    
    if hack12:
        hack1=font.render("hack xoa vat the",True,green)
        hack1=screen.blit(hack1,(240,200))
    if hack123:
        x_bird = 50
        y_bird = 350
        tube_velocity=2
        score=0 
    #kiem tra su va cham   
    tubes=[tube1,tube2,tube3]
    for tube in tubes:
        if bird.colliderect(tube):
            if tubeq:
                tube_velocity=0
                game_over=font.render('game over,Score: '+str(score),True,RED)
                screen.blit(game_over,(180,200))            
                replay=font1.render('press F11  to  continue',True,RED)
                screen.blit(replay,(230,320)) 
                pausing=True
                if game_over==True:
                    pygame.K_RIGHT=False
                    pygame.K_LEFT=False
                    pygame.K_UP=False
                    pygame.K_DOWN=False    
    #dieu khien bird
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing = False
        if event.type==pygame.KEYDOWN:                       
            if event.key==pygame.K_F8:
                hack12=True    
                hack1=True
                game_over=False
                tubez=False
                tubeq=False
            if event.key==pygame.K_F7:
                hack123=True 
                tubez=True 
                hack12=False  
                tubeq=True     
            if event.key==pygame.K_RIGHT:                
                x_bird+=22
            if event.key==pygame.K_LEFT:               
                x_bird-=22
            if event.key==pygame.K_DOWN:
                y_bird+=22
            if event.key==pygame.K_UP:
                y_bird-=22
            if x_bird + 100 > 700:      
                x_bird = 600
            if x_bird < 0:                
                x_bird = 0
            if y_bird + 100 > 400:
                y_bird = 300
            if y_bird < 0:
                y_bird = 0
            if hack123:
                x_bird = 50
                y_bird = 200
                x_colum=1000
                x_colum1=1111
                x_colum2=1222
                tube_velocity=3
                score=0
                hack123=False
    pygame.display.flip()
pygame.quit()

