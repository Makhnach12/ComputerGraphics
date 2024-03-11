import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT
from Lab2.Star import Star


def drawGrid(canvas):
    for i in range(0, WIDTH, 20):
        canvas.create_line(i, 0, i, WIDTH, fill="gray")
    for i in range(0, HEIGHT, 20):
        canvas.create_line(0, i, HEIGHT, i, fill="gray")


def drawAxes(canvas):
    canvas.create_line(WIDTH // 2, WIDTH, WIDTH // 2, 0, width=1,
                       arrow=tk.LAST)
    canvas.create_line(0, HEIGHT // 2, HEIGHT, HEIGHT // 2, width=1,
                       arrow=tk.LAST)


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LAB2.COM")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.star = Star(self.canvas, (WIDTH // 2, HEIGHT // 2))
        self.canvas.pack(side=tk.LEFT)
        self.down_button = tk.Button(self.root, text="↓", width=10,
                                     command=self.star.shiftDown)
        self.down_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 10)
        self.up_button = tk.Button(self.root, text="↑", width=10,
                                   command=self.star.shiftUp)
        self.up_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 40)
        self.left_button = tk.Button(self.root, text="←", width=1, height=3,
                                     command=self.star.shiftLeft)
        self.left_button.place(x=WIDTH + 10, y=HEIGHT // 10 - 38)

        right_button = tk.Button(self.root, text="→", width=1, height=3,
                                      command=self.star.shiftRight)
        right_button.place(x=WIDTH + 190, y=HEIGHT // 10 - 38)

        reflectOX = tk.Button(self.root, text="симметрия OX",
                                   command=self.star.reflectOX)
        reflectOX.place(x=WIDTH + 60, y=HEIGHT // 5)

        reflectOY = tk.Button(self.root, text="симметрия OY",
                              command=self.star.reflectOY)
        reflectOY.place(x=WIDTH + 60, y=HEIGHT // 5 - 20)


    def shiftStar(self, x_shift: int, y_shift: int):
        self.star.changeCoors(x_shift, y_shift)
