#its a snake game
import pygame
import sys
import random
import time
check_error=pygame.init()
#it outputs the numbers of errors and processes(6,0) second digit in tuple shows errors
if(check_error[1]>0):
    print("got {0} initializing errors, exiting.....".format(check_error[1]))
    sys.exit(-1)
else:
    print("pygame succesfully initalized")
#play surface
playsurface=pygame.display.set_mode((720,460))
pygame.display.set_caption("snake game")
#colors
red=pygame.Color(255,0,0)
green=pygame.Color(0,0,255)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
yellow=pygame.Color(255,145,0)
#fps
fpscontroller=pygame.time.Clock()
snakepos=[100,50]
snakebody=[[100,50],[90,50],[80,50]]
foodpos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodspawn=True

#direction
direction="RIGHT"
changeto=direction
score=0

#gameover fn
def gameover():
    myfont=pygame.font.SysFont("monaco",72)
    gosurf=myfont.render("game over!",True,red)
    gorect=gosurf.get_rect();
    gorect.midtop=(360,15)
    playsurface.blit(gosurf,gorect)
    showscore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit(0)
    
def showscore(choice=1):
    sfont=pygame.font.SysFont("monaco",24)
    ssurf=sfont.render("score:{0}:".format(score),True,black)
    srect=ssurf.get_rect()
    if choice==1:
        srect.midtop=(80,10)
    else:
        srect.midtop=(360,120)
    playsurface.blit(ssurf,srect)
    pygame.display.flip()
#main logic
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
        foodspawn=False
    else:
        snakebody.pop()
    #foodspawn
    if foodspawn==False:
        foodpos=[random.randrange(1,71)*10,random.randrange(1,45)*10]
    foodspawn=True
    #setting background color
    playsurface.fill(white)

    #drawing snake body and the food
    for pos in snakebody:
        if pos==snakebody[0]:
            pygame.draw.line(playsurface,green,(pos[0],pos[1]),(pos[0],pos[1]))
        else:
            pygame.draw.circle(playsurface,green,(pos[0],pos[1]),7)
    pygame.draw.circle(playsurface,yellow,(foodpos[0],foodpos[1]),7)

    #bound
    if snakepos[0]>710 or snakepos[0]<10:
        gameover()
    if snakepos[1]>450 or snakepos[1]<10:
        gameover()
    for block in snakebody[1:]:
        if snakepos[0]==block[0] and snakepos[1]==block[1]:
            gameover()
    pygame.display.flip()
    showscore()
    fpscontroller.tick(15)
    
        


         
