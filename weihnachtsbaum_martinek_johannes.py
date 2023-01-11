"""
© MARTINEK Johannes
"""

import turtle
import array

# the x and y coordinates to start drawing
x_zero = -22.5
y_zero = -180
# the arrays for the x and y coordinates of the different flames
x_flames = array.array("f", [])
y_flames = array.array("f", [])


# go to absolute coordinates, without drawing a line
def go_to(x: float, y: float):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def reset_settings():
    turtle.width(1)
    turtle.pencolor("black")
    turtle.fillcolor("#000000")


# draws a candle at given position
def draw_candle(x: float, y: float, go_to_zero: bool):
    go_to(x, y)
    turtle.fillcolor("#ff0000")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(37)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(37)
    turtle.left(90)
    turtle.end_fill()
    go_to(x + 10, y + 37)
    turtle.width(3)
    turtle.left(90)
    turtle.forward(7)
    turtle.right(90)
    reset_settings()
    x_flames.append(x + 10)
    y_flames.append(y + 44)
    if go_to_zero:
        go_to(x_zero, y_zero)


# draws a circle at a given position, with a specified color and radius
def draw_circle(x: float, y: float, hex_c: str, radius: int, go_to_zero: bool):
    go_to(x, y - radius)
    turtle.fillcolor(hex_c)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    if go_to_zero:
        go_to(x_zero, y_zero)


# draws the star
def draw_star():
    side_length = 45
    go_to(0, 180)
    turtle.fillcolor("#ffee00")
    turtle.begin_fill()
    turtle.right(36)
    turtle.forward(side_length)
    turtle.left(144)
    turtle.forward(side_length)
    turtle.right(72)
    turtle.forward(side_length)
    turtle.left(144)
    turtle.forward(side_length)
    turtle.right(72)
    turtle.forward(side_length)
    turtle.left(144)
    turtle.forward(side_length)
    turtle.right(72)
    turtle.forward(side_length)
    turtle.left(144)
    turtle.forward(side_length)
    turtle.right(72)
    turtle.forward(side_length)
    turtle.left(144)
    turtle.forward(side_length)
    turtle.end_fill()
    turtle.right(36)
    go_to(x_zero, y_zero)


# draw the flames specified in x_flames and y_flames
def draw_flames():
    i = 0
    for x_flame in x_flames:
        y_flame = y_flames[i]
        draw_circle(x_flame, y_flame, "#ffdd00", 7, False)
        go_to(x_flame, y_flame - 7)
        turtle.width(3)
        turtle.left(90)
        turtle.forward(7)
        turtle.right(90)
        reset_settings()
        i = i + 1
    go_to(x_zero, y_zero)


# draws a present at a given position, with specified width, height, ribbon_width, color and ribbon_color
def draw_present(x: float, y: float, width: int, height: int, ribbon_width: int, present_color: str, ribbon_color: str,
                 go_to_zero: bool):
    go_to(x, y)
    turtle.fillcolor(present_color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.pencolor(ribbon_color)
    turtle.width(ribbon_width)
    turtle.up()
    turtle.forward(width / 2)
    turtle.down()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    go_to(x, y + (height / 2))
    turtle.forward(width)
    reset_settings()
    if go_to_zero:
        go_to(x_zero, y_zero)


# draws a gingerbread_man at a given position
def draw_gingerbread_man(x: float, y: float, go_to_zero: bool):
    arm_length = 10
    leg_length = 12.5
    go_to(x-5, y-52)
    # body
    turtle.fillcolor("#996633")
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(leg_length)
    turtle.circle(5, 180)
    turtle.forward(leg_length + 10)
    turtle.right(90)
    turtle.forward(arm_length)
    turtle.circle(5, 180)
    turtle.forward(arm_length)
    turtle.right(90)
    turtle.forward(10)
    turtle.circle(15, 180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(arm_length)
    turtle.circle(5, 180)
    turtle.forward(arm_length)
    turtle.right(90)
    turtle.forward(leg_length + 10)
    turtle.circle(5, 180)
    turtle.forward(leg_length)
    turtle.right(90)
    turtle.end_fill()
    # mouth
    go_to(x-6, y - 27)
    turtle.right(90)
    turtle.pencolor("white")
    turtle.width(2)
    turtle.circle(6, 180)
    # eyes
    go_to(x - 0.5, y - 22)
    turtle.circle(1)
    go_to(x + 4.5, y - 22)
    turtle.circle(1)
    turtle.right(90)
    # buttons
    go_to(x, y - 41.5)
    turtle.circle(1)
    go_to(x, y - 47)
    turtle.circle(1)

    go_to(x, y-10)
    turtle.width(3)
    turtle.pencolor("black")
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)

    reset_settings()
    if go_to_zero:
        go_to(x_zero, y_zero)


# draws a snow_man at a given position
def draw_snow_man(x: float, y: float, go_to_zero: bool):
    go_to(x, y)

    # body
    turtle.circle(50)
    go_to(x, y + 100)
    turtle.circle(32.5)
    go_to(x, y + 165)
    turtle.circle(21)

    # buttons and face
    turtle.width(3)
    for i in range(1, 4):
        go_to(x, y + (25 * i))
        turtle.circle(1.5)
    for i in range(1, 3):
        go_to(x, y + 100 + (20 * i))
        turtle.circle(1.5)
    go_to(x - 11, y + 184)
    turtle.right(90)
    turtle.circle(11, 180)
    turtle.right(90)
    turtle.width(3.5)
    go_to(x - 6, y + 192.5)
    turtle.circle(1.7)
    go_to(x + 6, y + 192.5)
    turtle.circle(1.7)
    go_to(x, y + 183)
    turtle.pencolor("orange")
    turtle.width(4)
    turtle.circle(2)
    reset_settings()

    # arm right
    go_to(x + 32.5, y + 132.5)
    turtle.width(5)
    turtle.pencolor("brown")
    turtle.forward(47.5)
    turtle.up()
    turtle.backward(14.5)
    turtle.down()
    turtle.left(45)
    turtle.forward(14.5)
    turtle.up()
    turtle.backward(14.5)
    turtle.down()
    turtle.right(90)
    turtle.forward(14.5)
    turtle.left(45)
    reset_settings()

    # arm left
    go_to(x - 32.5, y + 132.5)
    turtle.width(5)
    turtle.pencolor("brown")
    turtle.backward(47.5)
    turtle.up()
    turtle.forward(14.5)
    turtle.down()
    turtle.left(45)
    turtle.backward(14.5)
    turtle.up()
    turtle.forward(14.5)
    turtle.down()
    turtle.right(90)
    turtle.backward(14.5)
    turtle.left(45)
    reset_settings()

    # hat
    turtle.width(4)
    go_to(x - 28.5, y + 202.5)
    turtle.forward(57)
    go_to(x - 17.5, y + 202.5)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.end_fill()
    reset_settings()

    # broom
    go_to(x + 72.5, y)
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.end_fill()
    go_to(x + 49.5, y + 170)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.end_fill()
    go_to(x + 53.7, y + 177.5)
    turtle.fillcolor("#a67b3f")
    turtle.begin_fill()
    turtle.forward(42.5)
    turtle.left(90)
    turtle.forward(11.3)
    turtle.left(90)
    turtle.forward(42.5)
    turtle.left(90)
    turtle.forward(11.3)
    turtle.left(90)
    turtle.end_fill()
    reset_settings()

    if go_to_zero:
        go_to(x_zero, y_zero)


# set speed
turtle.speed(0)
# go to start position
go_to(x_zero, y_zero)


"""
# height of the tree
height = 360

# test drawing
# left side
turtle.pencolor("blue")
turtle.left(90)
turtle.forward(height)
turtle.left(180)
turtle.up()
turtle.forward(height)
turtle.left(90)
turtle.down()
# middle
turtle.pencolor("red")
turtle.up()
turtle.forward(22.5)
turtle.down()
turtle.left(90)
turtle.forward(height)
turtle.up()
turtle.left(180)
turtle.forward(height)
turtle.right(90)
turtle.forward(22.5)
turtle.right(180)
# right side
turtle.pencolor("blue")
turtle.forward(45)
turtle.down()
turtle.left(90)
turtle.forward(height)
turtle.left(180)
turtle.up()
turtle.forward(height)
turtle.right(90)
turtle.forward(45)
turtle.right(180)
# end
turtle.pencolor("black")
turtle.down()
"""

# drawing instructions
# fill stem
turtle.fillcolor("#964B00")
turtle.begin_fill()
turtle.forward(45)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.end_fill()
# go to top start
go_to(145.5, -100)
turtle.left(135)
# fill top
turtle.fillcolor("#05ab42")
turtle.begin_fill()
turtle.forward(165)
turtle.right(135)
turtle.forward(80)
turtle.left(135)
turtle.forward(130)
turtle.right(135)
turtle.forward(55)
turtle.left(135)
turtle.forward(101)
turtle.left(90)
turtle.forward(101)
turtle.left(135)
turtle.forward(55)
turtle.right(135)
turtle.forward(130)
turtle.left(135)
turtle.forward(80)
turtle.right(135)
turtle.forward(165)
turtle.left(135)
turtle.forward(291)
turtle.end_fill()
# draw decorations
draw_snow_man(275, y_zero, True)
draw_circle(-85, -75, "#ffaa00", 10, False)
draw_circle(50, -65, "#00ffff", 10, False)
draw_circle(5, -45, "#ee00ff", 10, False)
draw_circle(40, 50, "#00ffff", 10, False)
draw_circle(-15, 70, "#ee00ff", 10, False)
draw_circle(-30, 125, "#00ffff", 10, False)
draw_circle(15, 140, "#ff0000", 10, True)
draw_gingerbread_man(-100, 16, False)
draw_gingerbread_man(71, 108, True)
draw_candle(0, 0, False)
draw_candle(-50, -70, False)
draw_candle(-75, 40, False)
draw_candle(50, -35, True)
draw_star()
draw_present(3, y_zero, 65, 65, 5, "#ff0000", "#ffee00", False)
draw_present(-80, y_zero, 45, 45, 3, "#ffee00", "#0000ff", False)
draw_present(-160, y_zero, 65, 65, 5, "#0000ff", "#ff8800", False)
draw_present(88, y_zero, 45, 45, 3, "#ff8800", "#00ff00", False)
draw_present(155, y_zero, 45, 45, 3, "#00ff00", "#ff0000", True)
draw_flames()

# end code
turtle.hideturtle()
turtle.done()
