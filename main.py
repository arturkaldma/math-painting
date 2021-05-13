from canvas import Canvas
from shapes import Square
from shapes import Rectangle

# Ask for canvas info and create a canvas
width = int(input("Enter canvas width: "))
height = int(input("Enter canvas height: "))
choice = {"white": (255, 255, 255), "black": (0, 0, 0)}
colors = input("Color white or black: ").lower()
canvas = Canvas(width, height, choice[colors])

while True:
    answer = input("Square, rectangle or quit?").lower()
    # Ask for square info and create a square
    if answer == "square":
        s_x = int(input("x position: "))
        s_y = int(input("y position: "))
        s_side = int(input("side length: "))
        red = int(input("How much of red?: "))
        green = int(input("How much of green?: "))
        blue = int(input("How much of blue?: "))
        s = Square(s_x, s_y, s_side, (red, green, blue))
        s.draw(canvas)

    # Ask for rectangle info and create a rectangle
    elif answer == "rectangle":
        r_x = int(input("x position: "))
        r_y = int(input("y position: "))
        r_height = int(input("height: "))
        r_width = int(input("width: "))
        red = int(input("How much of red?: "))
        green = int(input("How much of green?: "))
        blue = int(input("How much of blue?: "))
        r = Rectangle(r_x, r_y, r_height, r_width, (red, green, blue))
        r.draw(canvas)

    elif answer == "quit":
        break

canvas.make()