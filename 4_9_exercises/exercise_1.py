import turtle


def square(ninja):
    for _ in range(4):
        ninja.forward(20)
        ninja.left(90)

    ninja.penup()
    ninja.forward(40)
    ninja.pendown()


screen = turtle.Screen()
ninja = turtle.Turtle()

for _ in range(4):
    square(ninja)

screen.exitonclick()
