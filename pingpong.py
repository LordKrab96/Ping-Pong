import turtle
from random import choice, randint
import typing

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()
border.speed(0)
border.color("green")
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
border.goto(0, 300)
border.color("white")
border.setheading(270)

for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()

rocket_R = turtle.Turtle()
rocket_R.color("white")
rocket_R.shape("square")
rocket_R.shapesize(stretch_len=1, stretch_wid=5)
rocket_R.penup()
rocket_R.goto(450, 0)

rocket_L = turtle.Turtle()
rocket_L.color("white")
rocket_L.shape("square")
rocket_L.shapesize(stretch_len=1, stretch_wid=5)
rocket_L.penup()
rocket_L.goto(-450, 0)


def L_move_up():
    y = rocket_L.ycor() + 10
    if y > 250:
        y = 250
    rocket_L.sety(y)


def L_move_down():
    y = rocket_L.ycor() - 10
    if y < -250:
        y = -250
    rocket_L.sety(y)


def R_move_up():
    y = rocket_R.ycor() + 10
    if y > 250:
        y = 250
    rocket_R.sety(y)


def R_move_down():
    y = rocket_R.ycor() - 10
    if y < -250:
        y = -250
    rocket_R.sety(y)


FONT = ("Arial", 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.color("white")
s1.penup()
s1.setposition(-200, 300)
s1.write(score_a, font=FONT)

score_b = 0
s2 = turtle.Turtle(visible=False)
s2.color("white")
s2.penup()
s2.setposition(200, 300)
s2.write(score_b, font=FONT)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.speed(2)
ball.dx = 0.5
ball.dy = 0.5
ball.penup()

window.listen()
window.onkeypress(L_move_up, "w")
window.onkeypress(L_move_down, "s")
window.onkeypress(R_move_up, "Up")
window.onkeypress(R_move_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0, randint(-200, 200))
        ball.dx = choice([-0.4, -0.3, -0.2, 0.2, 0.3, 0.4])
        ball.dy = choice([-0.4, -0.3, -0.2, 0.2, 0.3, 0.4])

    if ball.xcor() <= -490:
        score_a += 1
        s1.clear()
        s1.write(score_a, font=FONT)
        ball.goto(0, randint(-200, 200))
        ball.dx = choice([-0.4, -0.3, -0.2, 0.2, 0.3, 0.4])
        ball.dy = choice([-0.4, -0.3, -0.2, 0.2, 0.3, 0.4])

    if ball.ycor() >= rocket_R.ycor() - 60 and ball.ycor() <= rocket_R.ycor() + 60 \
            and ball.xcor() >= rocket_R.xcor() - 7 and ball.xcor() <= rocket_R.xcor() + 7:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_L.ycor() - 60 and ball.ycor() <= rocket_L.ycor() + 60 \
            and ball.xcor() >= rocket_L.xcor() - 7 and ball.xcor() <= rocket_L.xcor() + 7:
        ball.dx = -ball.dx

window.mainloop()
