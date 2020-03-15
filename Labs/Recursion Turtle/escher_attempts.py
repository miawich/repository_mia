import turtle

# setting up turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.hideturtle()
my_turtle.speed(0)

# setting up screen
my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursive_star(x, y, heading, length, depth):
    if depth > 0:
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(heading)
        for i in range(5):
            my_turtle.forward(length)
            my_turtle.right(144)
        my_turtle.up()
        my_turtle.goto(-x, y)
        my_turtle.down()
        my_turtle.setheading(heading)
        for i in range(5):
            my_turtle.forward(length)
            my_turtle.right(144)
        my_turtle.up()
        my_turtle.goto(x, -y)
        my_turtle.down()
        my_turtle.setheading(heading)
        for i in range(5):
            my_turtle.forward(length)
            my_turtle.right(144)
        my_turtle.up()
        my_turtle.goto(-x, -y)
        my_turtle.down()
        my_turtle.setheading(heading)
        for i in range(5):
            my_turtle.forward(length)
            my_turtle.right(144)
        my_turtle.up()
        turtle_pos = my_turtle.pos()
        # my_turtle.goto(turtle_pos[0] + length * 2 / 3, turtle_pos[1] + length * 2 / 3)
        recursive_star(turtle_pos[0] + length / 2 , turtle_pos[1] + length / 2 , heading - 180, length * 9 / 24, depth - 1)
        recursive_star(turtle_pos[0] - length / 2, turtle_pos[1] + length / 2, heading - 180, length * 9 / 24,
                       depth - 1)
        recursive_star(turtle_pos[0] + length / 2, turtle_pos[1] - length / 2, heading - 180, length * 9 / 24,
                       depth - 1)
        recursive_star(turtle_pos[0] - length / 2, turtle_pos[1] - length / 2, heading - 180, length * 9 / 24,
                       depth - 1)


recursive_star(0, 0, 63, 400, 6)
