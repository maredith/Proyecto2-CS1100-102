# PRIMERA PARTE

# Importando elementos básicos
import turtle
import math
import random

# Creando la ventana
wn = turtle.Screen()
wn.bgcolor('black')

# Dibujando la primera ronda de círculos
Primero = turtle.Turtle()
Primero.speed(0)
Primero.color('white')
rotate = int(360)


def drawCircles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


        # Dibujando la segunda ronda de círculos


drawSpecial(Primero, 100, 10)
Segundo = turtle.Turtle()
Segundo.speed(0)
Segundo.color('yellow')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


        # Dibujando la tercera ronda de círculos


drawSpecial(Segundo, 100, 10)
Tercero = turtle.Turtle()
Tercero.speed(0)
Tercero.color('blue')
rotate = int(80)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


        # Dibujando la cuarta ronda de círculos


drawSpecial(Tercero, 100, 10)
Cuarto = turtle.Turtle()
Cuarto.speed(0)
Cuarto.color('orange')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


        # Dibujando la quinta ronda de círculos


drawSpecial(Cuarto, 100, 10)
Quinto = turtle.Turtle()
Quinto.speed(0)
Quinto.color('pink')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 20


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Quinto, 100, 10)
# FINAL DE LA PRIMERA PARTE

# SEGUNDA PARTE

# Propiedades del dibujador
turtle.speed(0)
turtle.color('blue')
turtle.up()
turtle.goto(200, 150)

# Se define la función general
phi = (1 + math.sqrt(5)) / 2
i = 360 / math.pi
t = turtle
t.down()

for x in range(144):
    t.right(i)
    u = i
    t.forward(400)

# Cambio de color a rojo
turtle.color('red')

for x in range(233):
    t.right(i)
    u = i
    t.forward(400)

# Cambio de color a verde
turtle.color('green')

for x in range(144):
    t.right(i)
    u = i
    t.forward(400)

# Cambio de color a blanco
turtle.color('white')

for x in range(144):
    t.right(i)
    u = i
    t.forward(400)
# FINAL DE LA SEGUNDA PARTE

# TERCERA PARTE

turtle.speed(0)
turtle.color('orange')


# create and run turtle

def square(size):
    for i in range(4):
        turtle.forward(size)

        turtle.left(60)


for i in range(30):
    square(5 * i)

    turtle.left(i)

# FINAL DE LA TERCERA PARTE


turtle.penup()
turtle.goto(250, 250)
turtle.pendown()

# CUARTA PARTE
# Configurar modo aleatorio
from random import randint

# Propiedades del dibujador
size = 20
circles = 1
turtle.speed(0)


def move(length, angle):
    turtle.right(angle)
    turtle.forward(length)


def hex():
    turtle.pendown()
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.begin_fill()
    for i in range(6):
        move(size, -200)
    turtle.end_fill()
    turtle.penup()


# start
turtle.penup()

for circle in range(circles):
    if circle == 0:
        hex()
        move(size, -60)
        move(size, -60)
        move(size, -60)
        move(0, 180)
    for i in range(6):
        move(0, 60)
        for j in range(circle + 1):
            hex()
            move(size, -60)
            move(size, 60)
        move(-size, 0)
    move(-size, 60)
    move(size, -120)
    move(0, 60)

# FINAL DE CUARTA PARTE


# QUINTA PARTE (REPETICIÓN DE LA CUARTA PARTE)
size = 20
circles = 1
turtle.speed(0)


def move(length, angle):
    turtle.right(angle)
    turtle.forward(length)


def hex():
    turtle.pendown()
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.begin_fill()
    for i in range(6):
        move(size, -200)
    turtle.end_fill()
    turtle.penup()


# start
turtle.penup()

for circle in range(circles):
    if circle == 0:
        hex()
        move(size, -60)
        move(size, -60)
        move(size, -60)
        move(0, 180)
    for i in range(6):
        move(0, 60)
        for j in range(circle + 1):
            hex()
            move(size, -60)
            move(size, 60)
        move(-size, 0)
    move(-size, 60)
    move(size, -120)
    move(0, 90)

turtle.done()