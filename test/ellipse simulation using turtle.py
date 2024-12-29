import turtle
from math import *

win = turtle.Screen()
win.setup(600, 600)
win.setworldcoordinates(0, 0, 600, 600)
win.bgcolor("grey")

t = turtle.Turtle()
point = turtle.Turtle()
t.speed(0)
point.speed(0)
t.shape("circle")
point.shape("circle")
point.color("black")
t.shapesize(2, 2, 1)
t.color("red")
point.penup()
point.setpos(400, 300)

a = 200
e = 1/1.4

c = a*e

p = 0

def get_r(x):
    r = a*(1-e**2)/(1+e*cos(x))
    return r

def r_v(p):
    return 1/(get_r(p)**2)

running = True
while running:
    p = p + r_v(p)*500
    x = 400 + get_r(p)*cos(p)
    y = 300 + get_r(p)*sin(p)
    t.setpos(x, y)
win.mainloop()