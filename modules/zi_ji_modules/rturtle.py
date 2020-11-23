import turtle
p = turtle.Pen()
def begin_fill():
    p.begin_fill()
def end_fill():
    p.end_fill()
def lookpen():
    p.showturtle()
def nlookpen():
    p.hideturtle()
def clear():
    p.clear()
def delete():
    p.reset()
def color(c1 = 'black',c2 = 'white'):
    if c2 == 'white':
        c2 = c1
    p.color(c1,c2)
def home():
    p.home()
def goto(x,y):
    p.goto(x,y)
def forward(l):
    p.forward(l)
def penunder():
    turtle.undo()
def go_y(y):
    p.sety(y)
def go_x(x):
    p.setx(x)
def jcircle(r,extent = None,steps = None):
    p.circle(r, extent, steps)
def njcircle(r,d = 360):
    p.circle(r, d)
def right(d):
    p.right(d)
def left(d):
    p.left(d)
def jiaodu(d):
    p.setheading(d)
def dian(z = 3):
        p.dot(z)
def tu(long,s):
    i = 1
    d = 360 / s
    while i <= s:
        p.forward(long)
        p.right(d)
        i = i + 1
def done():
    turtle.done()
def speed(sp):
    p.speed(sp)
def write(f,font):
    p.write(f,font = font)
def pendown():
    p.pendown()
def penup():
    p.penup()