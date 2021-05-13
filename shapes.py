class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, a, b, color):
        self.color = color
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.b] = self.color