import turtle

harr = turtle.Turtle()
def teleport(harr, x, y):
  harr.penup() #поднять "ручку" - отключение отрисовки за черепашкой
  harr.goto(x,y) #перемещение черепашки в указанные координаты x и y
  harr.pendown() #опустить "ручку" - вкключение отрисовки за черепашкой
  
def set_color(clr):
  harr.color(clr)
  
def square(harr, x, y, size):
  teleport(harr, x, y)
  for _ in range(4):
    harr.forward(size)
    harr.left(90)
  

def triangle(harr, x, y, size):
  teleport(harr, x, y)
  for _ in range(3):
    harr.forward(size)
    harr.left(120)

def circle(harr, x, y, size):
  teleport(harr, x, y)
  harr.circle(size)

def hexagonal(harr, x, y, size):
  teleport(harr, x, y)
  for _ in range(6):
    harr.forward(size)
    harr.left(60)

def multiangle(harr, size, x, y, angles):    # 2Rsin(180/n)
  teleport(harr, x, y)
  for _ in range(angles):
    harr.forward(size)
    harr.left(360/angles)

set_color("red")
square(harr, 0, 0, 75)
triangle(harr, 90, 0, 30)
circle(harr, -90, 0, 40)
multiangle(harr, 180, 0, 15, 20)
hexagonal(harr, 0, -180, 75)
                                                                                           