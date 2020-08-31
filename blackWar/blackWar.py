# 完整演示
import pygame,sys,time,random
import secret
pygame.init()
screen = pygame.display.set_mode((800, 650))
pygame.display.set_caption("黑客帝国")
screen.fill((0, 0, 0))
pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.play(-1)
picList = ["warning1.png", "warning2.png", "warning3.png",
            "warning4.png", "warning5.png", "warning11.png"]
imgList = []
for i in range(6):
    myImg = pygame.image.load(picList[i]).convert()
    imgList.append(myImg)

imgNum = 0
a = 0
secret.rain(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                a = 0
                imgNum = imgNum+1
                if imgNum == len(imgList):
                    imgNum = 0
    image = imgList[imgNum]
    a = a+1
    if a > 255:
        a = 0
    image.set_alpha(a)
    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))
    pygame.display.update()
    time.sleep(0.01)