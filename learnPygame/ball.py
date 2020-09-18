import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURTF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('HELLO WORLD')

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 30
fpsClock = pygame.time.Clock()

cherryImg = pygame.image.load('0.png')
cherryX = cherryY = 10
direction = 'right'

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, RED, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
#DISPLAYSURTF.fill(WHITE)
#pygame.draw.polygon(DISPLAYSURTF, RED, ((146,0),(291, 106),(236,277)))
while True:
    DISPLAYSURTF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print('x is ' + str(cherryX))
            if event.key == pygame.K_LEFT:
                cherryX -= 10
            elif event.key == pygame.K_RIGHT:
                cherryX += 10
            elif event.key == pygame.K_UP:
                cherryY -= 10
            elif event.key == pygame.K_DOWN:
                cherryY += 10
    DISPLAYSURTF.blit(cherryImg, (cherryX, cherryY))
    DISPLAYSURTF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    fpsClock.tick(FPS)