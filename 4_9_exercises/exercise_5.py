import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

# Speed up to maximum
tess.speed(0)

for step in range(100):
    tess.forward(step * 5)
    # tess.right(90)
    tess.right(89)

screen.exitonclick()
