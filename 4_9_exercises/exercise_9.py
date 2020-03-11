import turtle


def draw_star(drawing_turtle):
    for _ in range(5):
        drawing_turtle.forward(100)
        drawing_turtle.right(144)


screen = turtle.Screen()
tess = turtle.Turtle()

draw_star(tess)

screen.exitonclick()
