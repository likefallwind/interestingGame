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

    if direction == 'right':
        cherryX += 5
        if cherryX == 280:
            direction = 'down'
    elif direction == 'down':
        cherryY += 5
        if cherryY == 220:
            direction = 'left'
    elif direction == 'left':
        cherryX -= 5
        if cherryX == 10:
            direction = 'up'
    else:
        cherryY -= 5
        if cherryY == 10:
            direction = 'right'

    DISPLAYSURTF.blit(cherryImg, (cherryX, cherryY))
    DISPLAYSURTF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)