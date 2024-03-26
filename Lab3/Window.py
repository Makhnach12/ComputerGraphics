import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab3.Circle import Circle
from Lab3.Line import Line

isLineDrown = False


def cleanEntry(entry: list):
    for elem in entry:
        elem.delete(0, tk.END)


def printDots(line):
    line.bresenhamAlgorithm()
    line.printDots()


def printDotsCircle(circle):
    circle.bresenhamAlgorithm()
    circle.printDots()


class WindowCircle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LAB3_2.COM")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.circle = Circle(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.canvas.pack(side=tk.LEFT)

        label_above_button = tk.Label(self.root, text="Координаты центра")
        label_above_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 30)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 10)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 30, y=HEIGHT // 10 + 10)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 - 10)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 130, y=HEIGHT // 10 + 10)

        label_above_button = tk.Label(self.root, text="Радиус окружности")
        label_above_button.place(x=WIDTH + 70, y=HEIGHT // 10 + 40)

        entryR = tk.Entry(self.root, width=10)
        entryR.place(x=WIDTH + 80, y=HEIGHT // 10 + 60)

        createLineButton = tk.Button(self.root, text='задать окружность',
                                     command=lambda: self.circle.createCircle(
                                         Dot(int(entryX.get()) * CELL_SIZE,
                                             int(entryY.get()) * CELL_SIZE),
                                         int(entryR.get()) * CELL_SIZE
                                     ))
        cleanEntry([entryX, entryY, entryR])
        createLineButton.place(x=WIDTH + 50, y=HEIGHT // 10 + 90)

        rastrButton = tk.Button(self.root, text="Растеризация",
                                command=lambda: printDots(self.circle))
        rastrButton.place(x=WIDTH + 65, y=HEIGHT // 10 + 120)


def openWindowCircle():
    win = WindowCircle()
    win.root.mainloop()


class WindowLine:
    def __init__(self):
        global isLineDrown
        self.root = tk.Tk()
        self.root.title("LAB3_1.COM")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.line = Line(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        # self.canvas.create_line((0, 0), (1, 1), fill='red', width=2)
        self.canvas.pack(side=tk.LEFT)

        label_above_button = tk.Label(self.root, text="Координаты начала")
        label_above_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 30)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 10)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 30, y=HEIGHT // 10 + 10)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 - 10)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 130, y=HEIGHT // 10 + 10)

        label_above_button = tk.Label(self.root, text="Координаты конца")
        label_above_button.place(x=WIDTH + 60, y=HEIGHT // 10 + 40)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 + 60)

        entryX2 = tk.Entry(self.root, width=10)
        entryX2.place(x=WIDTH + 30, y=HEIGHT // 10 + 80)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 + 60)

        entryY2 = tk.Entry(self.root, width=10)
        entryY2.place(x=WIDTH + 130, y=HEIGHT // 10 + 80)
        createLineButton = tk.Button(self.root, text='задать прямую',
                                     command=lambda: self.line.createLine(
                                         Dot(int(entryX.get()) * CELL_SIZE,
                                             int(entryY.get()) * CELL_SIZE),
                                         Dot(int(entryX2.get()) * CELL_SIZE,
                                             int(entryY2.get()) * CELL_SIZE)
                                     ))
        cleanEntry([entryX, entryY2, entryX2, entryY])
        createLineButton.place(x=WIDTH + 70, y=HEIGHT // 10 + 110)

        reflectOX = tk.Button(self.root, text="симметрия OY",
                              command=self.line.reflectOX)
        reflectOX.place(x=WIDTH + 70, y=HEIGHT // 10 + 140)

        reflectOY = tk.Button(self.root, text="симметрия OX",
                              command=self.line.reflectOY)
        reflectOY.place(x=WIDTH + 70, y=HEIGHT // 10 + 170)

        reflect = tk.Button(self.root, text="симметрия по прямой",
                            command=self.line.reflect)
        reflect.place(x=WIDTH + 48, y=HEIGHT // 10 + 200)

        offsetButton = tk.Button(self.root, text="смещение к началу",
                                 command=self.line.offsetLineToDot)
        offsetButton.place(x=WIDTH + 55, y=HEIGHT // 10 + 230)

        rastrButton = tk.Button(self.root, text="Растеризация",
                                command=lambda: printDots(self.line))
        rastrButton.place(x=WIDTH + 75, y=HEIGHT // 10 + 260)

        startPos = tk.Button(self.root, text="Вернуть начальное положение",
                             command=self.line.goStartPos)
        startPos.place(x=WIDTH + 30, y=HEIGHT // 10 + 290)

        startPos = tk.Button(self.root, text="Открыть растеризацию окружности",
                             command=openWindowCircle)
        startPos.place(x=WIDTH + 10, y=HEIGHT // 10 + 320)
