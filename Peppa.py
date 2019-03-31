import turtle

def drawNose():
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    turtle.begin_fill()
    a=0.4
    for i in range(120):
       if 0<=i<30 or 60<=i<90:
           a=a+0.08
           turtle.lt(3)
           turtle.fd(a)
       else:
           a=a-0.08
           turtle.lt(3)
           turtle.fd(a)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(25)
    turtle.seth(0)
    turtle.fd(10)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0)
    turtle.fd(20)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()


def drawHead():
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(41)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(180)
    turtle.circle(300, -30)
    turtle.circle(100, -60)
    turtle.circle(80, -100)
    turtle.circle(150, -20)
    turtle.circle(60, -95)
    turtle.seth(161)
    turtle.circle(-300, 15)
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    a=0.4
    for i in range(60):
       if 0<=i<30 or 60<=i<90:
           a=a+0.08
           turtle.lt(3)
           turtle.fd(a)
       else:
           a=a-0.08
           turtle.lt(3)
           turtle.fd(a)
    turtle.end_fill()


def drawEar():
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-7)
    turtle.seth(0)
    turtle.fd(70)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 54)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-12)
    turtle.seth(0)
    turtle.fd(30)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 56)
    turtle.end_fill()


def drawEyes():
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-20)
    turtle.seth(0)
    turtle.fd(-95)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-25)
    turtle.seth(0)
    turtle.fd(40)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()


def drawBlush():
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-95)
    turtle.seth(0)
    turtle.fd(65)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def drawLip():
    turtle.color(239, 69, 19)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(15)
    turtle.seth(0)
    turtle.fd(-100)
    turtle.pd()
    turtle.seth(-80)
    turtle.circle(30, 40)
    turtle.circle(40, 80)

def drawBody():
    turtle.color("red", (255, 99, 71))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-20)
    turtle.seth(0)
    turtle.fd(-78)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(-130)
    turtle.circle(100, 10)
    turtle.circle(300, 30)
    turtle.seth(0)
    turtle.fd(230)
    turtle.seth(90)
    turtle.circle(300, 30)
    turtle.circle(100, 3)
    turtle.color((255, 155, 192), (255, 100, 100))
    turtle.seth(-135)
    turtle.circle(-80, 63)
    turtle.circle(-150, 24)
    turtle.end_fill()


def drawHand():
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-40)
    turtle.seth(0)
    turtle.fd(-27)
    turtle.pd()
    turtle.seth(-160)
    turtle.circle(300, 15)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(15)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.seth(-10)
    turtle.circle(-20, 90)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(30)
    turtle.seth(0)
    turtle.fd(237)
    turtle.pd()
    turtle.seth(-20)
    turtle.circle(-300, 15)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(20)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.seth(-170)
    turtle.circle(20, 90)

def drawFoot():
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-75)
    turtle.seth(0)
    turtle.fd(-180)
    turtle.pd()
    turtle.seth(-90)
    turtle.fd(40)
    turtle.seth(-180)
    turtle.color("black")
    turtle.pensize(15)
    turtle.fd(20)
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(40)
    turtle.seth(0)
    turtle.fd(90)
    turtle.pd()
    turtle.seth(-90)
    turtle.fd(40)
    turtle.seth(-180)
    turtle.color("black")
    turtle.pensize(15)
    turtle.fd(20)

def drawTail():
    turtle.pensize(4)
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(70)
    turtle.seth(0)
    turtle.fd(95)
    turtle.pd()
    turtle.seth(0)
    turtle.circle(70, 20)
    turtle.circle(10, 330)
    turtle.circle(70, 30)

def main():
    turtle.pensize(4)
    turtle.colormode(255)
    turtle.color((255, 155, 192), "pink")
    turtle.setup(1000, 600)
    turtle.speed(10)
    drawNose()
    drawHead()
    drawEar()
    drawEyes()
    drawBlush()
    drawLip()
    drawBody()
    drawHand()
    drawFoot()
    drawTail()
    turtle.done()

if __name__ == '__main__':
    main()