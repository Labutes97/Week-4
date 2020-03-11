import turtle


def square(ninja, size):
    ninja.penup()
    ninja.backward(10)
    ninja.right(90)
    ninja.forward(10)
    ninja.left(90)
    ninja.pendown()

    for _ in range(4):
        ninja.forward(size)
        ninja.left(90)


screen = turtle.Screen()
ninja = turtle.Turtle()

for n in range(1, 6):
    square(ninja, n * 20)

screen.exitonclick()
