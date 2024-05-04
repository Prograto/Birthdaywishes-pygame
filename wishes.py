import pygame
from pygame import mixer
import time
screen = pygame.display.set_mode([390,650])
pygame.display.set_caption("Bunny😊 Ka Birthday!🎂")
#initializing
pygame.init()
mixer.init()
clock = pygame.time.Clock()
#music
mixer.music.load("bd.mp3")
mixer.music.set_volume(0.8)
mixer.music.play(loops=-1)
#images
bunny = pygame.image.load("bunny.jpg")
sbunny = pygame.image.load("Birthday.jpg")
deco = pygame.image.load("deco.png")
text = pygame.image.load("bw.png")
pos = [650,650,-400,600]
c = 0
time.sleep(6)
while True:
    if pos[0]>0:
        pos[0] -= 5
    if pos[0]==0 and pos[1]>0:
        pos[1] -=5
    elif pos[2]<0:
        pos[2] +=5
    if pos[1]==0 and pos[3]>300:
        pos[3] -= 5



    screen.blit(bunny,[0,pos[0]])
    screen.blit(sbunny,[0,pos[1]])
    screen.blit(deco, [0, pos[2]])
    screen.blit(text, [0, pos[3]])
    pygame.display.update()
    clock.tick(30)
