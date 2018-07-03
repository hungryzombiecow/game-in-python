import pygame
import os
import sys
import random
import time
check=pygame.init()
if(check[1]>0):
    print('pygame can\'t be successfully initialized')
    sys.exit(0)
else:
    print('pygame successfully initialized')
playsurface=pygame.display.set_mode((800,600))
pygame.display.set_caption("snake game")
"""#colors
blue=pygame.Color(0,128,0)

#loading background music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)      #for looping -1 means it,ll keep on playing endlessly 2 means it'll play 2 times
image=pygame.image.load("bg.jpg")
img=pygame.transform.scale(image,(800,600))
playsurface.blit(img,(0,0))
#displaying snake image
image=pygame.image.load("snake.jpg")
img=pygame.transform.scale(image,(500,150))
#display=pygame.display.get_surface()

playsurface.blit(img,(150,100))
pygame.display.update()"""
#gameover fn
def gameover(score):
    #carsh with wall music
    pygame.mixer.music.load("walls.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)
    #displaying game over and score text
    myfont=pygame.font.SysFont("monaco",72)
    gosurf=myfont.render("game over!",True,pygame.Color(255,0,0))
    rsurf=myfont.render("click anywhere to restart",True,pygame.Color(0,0,0))
    rrect=rsurf.get_rect()
    gorect=gosurf.get_rect();
    rrect.midtop=(360,300)
    gorect.midtop=(360,15)
    playsurface.blit(rsurf,rrect)
    playsurface.blit(gosurf,gorect)
    showscore(score,0)
    pygame.display.flip()
    #print(pygame.event.get())
    time.sleep(2)
    #gameover music
    pygame.mixer.music.load("gameover.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)
    while 1:
        for event in pygame.event.get():
            print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                homepage()
        pygame.display.flip()
    """time.sleep(4)
    pygame.quit()
    sys.exit(0)
    """
def showscore(score,choice=1):
    sfont=pygame.font.SysFont("monaco",32)
    ssurf=sfont.render("score:{0}:".format(score),True,pygame.Color(0,0,0))
    srect=ssurf.get_rect()
    if choice==1:
        srect.midtop=(80,10)
    else:
        srect.midtop=(360,220)
    playsurface.blit(ssurf,srect)
    pygame.display.flip()
#main logic
def logic(f=15):
    #play surface
    playsurface.fill(pygame.Color(0,128,0))
    #colors
    red=pygame.Color(255,0,0)
    green=pygame.Color(0,0,255)
    black=pygame.Color(0,0,0)
    white=pygame.Color(255,255,255)
    yellow=pygame.Color(255,255,0)
    #fps
    fpscontroller=pygame.time.Clock()
    snakepos=[100,50]
    snakebody=[[100,50],[90,50],[80,50]]
    foodpos=[random.randrange(4,72)*10,random.randrange(4,46)*10]
    foodspawn=True

    #direction
    direction="RIGHT"
    changeto=direction
    score=0
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==ord('d'):
                    changeto='RIGHT'
                if event.key==pygame.K_LEFT or event.key==ord('a'):
                    changeto='LEFT'
                if event.key==pygame.K_UP or event.key==ord('W'):
                    changeto='UP'
                if event.key==pygame.K_DOWN or event.key==ord('S'):
                    changeto='DOWN'
                if event.key==pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.EVENT(QUIT))
        #validation of direction
        if changeto=='RIGHT' and not direction=='LEFT':
             direction='RIGHT'
        if changeto=='LEFT' and not direction=='RIGHT':
            direction='LEFT'
        if changeto=='UP' and not direction=='DOWN':
            direction='UP'
        if changeto=='DOWN' and not direction=='UP':
            direction='DOWN'

            #update snake pos [x,y]
        if direction=='RIGHT':
            snakepos[0]+=10
        if direction=='LEFT':
            snakepos[0]-=10
        if direction=='UP':
            snakepos[1]-=10
        if direction=='DOWN':
            snakepos[1]+=10

        #snakebody mechanis
        snakebody.insert(0,list(snakepos))
        if snakepos[0]==foodpos[0] and snakepos[1]==foodpos[1]:
            score+=1
            pygame.mixer.music.load("eating.wav")
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(1)
            foodspawn=False
        else:
            snakebody.pop()
        #foodspawn
        if foodspawn==False:
            foodpos=[random.randrange(1,72)*10,random.randrange(1,45)*10]
        foodspawn=True
        # background coulour
        playsurface.fill(pygame.Color(0,128,0))
        for pos in snakebody:
            if pos==snakebody[0]:
                pygame.draw.line(playsurface,green,(pos[0],pos[1]),(pos[0],pos[1]))
            else:
                pygame.draw.circle(playsurface,green,(pos[0],pos[1]),7)
        pygame.draw.circle(playsurface,pygame.Color(255,50,0),(foodpos[0],foodpos[1]),7)
        pygame.display.flip()
        #gameover

        #bound
        if snakepos[0]>810 or snakepos[0]<0:
            gameover(score)
        if snakepos[1]>610 or snakepos[1]<0:
            gameover(score)
        for block in snakebody[1:]:
            if snakepos[0]==block[0] and snakepos[1]==block[1]:
                gameover(score)
        pygame.display.flip()
        showscore(score)
        cond=8
        if(score>cond):
            f+=1
            cond+=2
        fpscontroller.tick(f)
def homepage():
  #colors
  blue=pygame.Color(0,128,0)
 #loading background music
  pygame.mixer.music.load("music.mp3")
  pygame.mixer.music.set_volume(0.5)
  pygame.mixer.music.play(-1)      #for looping -1 means it,ll keep on playing endlessly 2 means it'll play 2 times
  image=pygame.image.load("bg.jpg")   
  img=pygame.transform.scale(image,(800,600))
  playsurface.blit(img,(0,0))
  #displaying snake image
  image=pygame.image.load("snake.jpg")
  img=pygame.transform.scale(image,(500,150))
  #display=pygame.display.get_surface()

  playsurface.blit(img,(150,100))
  pygame.display.update()
    #buttons
  while 1:
        mouse=pygame.mouse.get_pos()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (480+60)>mouse[0]>360 and 350>mouse[1]>300:
                pygame.draw.rect(playsurface,pygame.Color(0,200,0),pygame.Rect(360,300,120,50))
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.set_volume(0)
                    logic()
            else:
                pygame.draw.rect(playsurface,pygame.Color(0,0,255),pygame.Rect(360,300,120,50))
        sfont=pygame.font.SysFont("monaco",24)
        ssurf=sfont.render("Start..",True,pygame.Color(0,0,0))
        srect=ssurf.get_rect()
        srect.midtop=(420,320)
        playsurface.blit(ssurf,srect)

        #exit button
        if (480+60)>mouse[0]>300 and 450>mouse[1]>400:
            pygame.draw.rect(playsurface,pygame.Color(0,200,0),pygame.Rect(360,400,120,50))
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                quit()
                sys.exit(0)
        else:
            pygame.draw.rect(playsurface,pygame.Color(0,0,255),pygame.Rect(360,400,120,50))
    

        sfont=pygame.font.SysFont("monaco",24)
        ssurf=sfont.render("Exit..",True,pygame.Color(0,0,0))
        srect=ssurf.get_rect()
        srect.midtop=(420,420)
        playsurface.blit(ssurf,srect)

    #displaying credits
        sfont=pygame.font.SysFont("monaco",24)
        ssurf=sfont.render("Developed by:KARTIKEY DUBEY",True,pygame.Color(128,128,128))
        surf=sfont.render("Developed by:KARTIKEY DUBEY",True,pygame.Color(0,128,0))
        srect=ssurf.get_rect()
        ssrect=surf.get_rect()
        srect.midtop=(345,120)
        ssrect.midtop=(145,580)
        playsurface.blit(surf,srect)
        playsurface.blit(ssurf,ssrect)
        pygame.display.update()
homepage()

time.sleep(10)
pygame.quit()
sys.exit(0)
