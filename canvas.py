import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color
        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        self.data[:] = self.color


    def make(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save("files/canvas.png")