'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''
import turtle

# setting up turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.hideturtle()
my_turtle.speed(0)

# setting up screen
my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursive_h(x, y, length, depth):
    if depth > 0:
        my_turtle.setheading(0)
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(length + x, y)
        my_turtle.goto(length + x, length + y)
        my_turtle.up()
        my_turtle.goto(length + x, y)
        my_turtle.down()
        my_turtle.goto(length + x, -length + y)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(-length + x, y)
        my_turtle.goto(-length + x, length + y)
        my_turtle.up()
        my_turtle.goto(-length + x, y)
        my_turtle.down()
        my_turtle.goto(-length + x, -length + y)
        my_turtle.up()
        my_turtle.goto(x, y)
        recursive_h(x + length, y + length, length / 2, depth - 1)
        recursive_h(x + length, y - length, length / 2, depth - 1)
        recursive_h(x - length, y + length, length / 2, depth - 1)
        recursive_h(x - length, y - length, length / 2, depth - 1)


recursive_h(0, 0, 100, 4)
my_screen.clear()


def recursive_escher(x, y, heading, length, depth):
    if depth > 0:
        my_turtle.setheading(heading)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        for i in range(4):
            my_turtle.forward(length)
            my_turtle.right(90)
        my_turtle.forward(length / 2)
        turtle_pos = my_turtle.pos()
    recursive_escher(turtle_pos[0], turtle_pos[1], heading - 45, length * 45/64, depth - 1)


recursive_escher(-250, 250, 0, 500, 16)

my_screen.clear()


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
        turtle_pos2 = my_turtle.pos()
        # my_turtle.goto(turtle_pos[0] + length * 2 / 3, turtle_pos[1] + length * 2 / 3)
        recursive_star(turtle_pos2[0] + length / 2 , turtle_pos2[1] + length / 2 , heading - 180, length * 9 / 24, depth - 1)
        recursive_star(turtle_pos2[0] - length / 2, turtle_pos2[1] + length / 2, heading - 180, length * 9 / 24,
                       depth - 1)
        recursive_star(turtle_pos2[0] + length / 2, turtle_pos2[1] - length / 2, heading - 180, length * 9 / 24,
                       depth - 1)
        recursive_star(turtle_pos2[0] - length / 2, turtle_pos2[1] - length / 2, heading - 180, length * 9 / 24,
                       depth - 1)


recursive_star(0, 0, 63, 400, 6)

