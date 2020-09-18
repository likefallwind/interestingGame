from turtle import *

def writeText(text, t, sc):
    sc.bgcolor("white")
    t.color("black")
    t.write(text, align="center", font = ["Arial", 50, "normal"])
    sc.delay(300)
    t.clear()

def showImg(img, t, sc):
    sc.bgpic(img)
    sc.delay(500)
    t.clear()

def showAll():
    sc = Screen()
    sc.setup(720,1280)
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0,300)

    t.clear()

    writeText("这个帅哥是谁？", t, sc)
    showImg("1.png", t, sc)
    writeText("看不清楚？", t, sc)
    writeText("还有一个照片！", t, sc)
    showImg("2.png", t, sc)
    writeText("对!", t, sc)
    writeText("这个帅哥就是", t, sc)
    writeText("大名鼎鼎的", t, sc)
    showImg("3.jpg", t, sc)
    writeText("王一博！", t, sc)
    writeText("图片发错了", t, sc)
    showImg("4.jpg", t, sc)
    writeText("更帅！")

if __name__ == '__main__':
    showAll()
