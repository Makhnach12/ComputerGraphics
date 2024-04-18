import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT, MIDDLE
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab4.Polygon import Polygon, checkerDotInList
from Lab4.Window import printDot

EPS: float = 0.3


def addInsideDot(stack, fillDots, dot, canvas):
    stack.append(dot)
    fillDots.append(printDot(canvas, dot, c='orange'))


class WindowFill:
    def __init__(self):
        self.lines = []
        self.stackInsideDots = []
        self.fillDots = []
        self.fillDotsCanvas = []
        self.root = tk.Tk()
        self.root.title("LAB5")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.polygon = Polygon(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.canvas.pack(side=tk.LEFT)

        def click(event):
            x, y = event.x, event.y
            print(x, y)
            if not 0 <= x < 600 or not 0 <= y < 600:
                return
            normX, normY = x - MIDDLE[0], MIDDLE[1] - y
            xCell, yCell = normX // 20, normY // 20
            if abs(abs(normX / 20) - abs(xCell)) > 0.5:
                xCell += 1
            if abs(abs(normY / 20) - abs(yCell)) > 0.5:
                yCell += 1
            if abs(abs(normX // 20) - abs(normX / 20)) < EPS:
                self.polygon.addDot(Dot(xCell * CELL_SIZE, yCell * CELL_SIZE),
                                    printBord=True)

        self.canvas.bind('<Button-1>', click)
        tk.Button(self.root, text='Сброс', command=self.deleteAll).place(
            x=WIDTH + 90,
            y=HEIGHT // 10 + 100
        )

        label_above_button = tk.Label(self.root, text="Координаты внутренней "
                                                      "точки")
        label_above_button.place(x=WIDTH + 27, y=HEIGHT // 10 - 30)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 10)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 30, y=HEIGHT // 10 + 10)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 - 10)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 130, y=HEIGHT // 10 + 10)

        tk.Button(self.root, text='Задать точку',
                  command=lambda:
                  addInsideDot(self.stackInsideDots, self.fillDotsCanvas,
                               Dot(int(entryX.get()) * CELL_SIZE,
                                   int(entryY.get()) * CELL_SIZE), self.canvas)
                  ).place(x=WIDTH + 70, y=HEIGHT // 10 + 40)

        tk.Button(self.root, text='Закрасить',
                  command=lambda:
                  self.completion()
                  ).place(x=WIDTH + 77, y=HEIGHT // 10 + 70)

    def addPolygon(self, polygonType, Dots: list[Dot]):
        self.polygon = polygonType(self.canvas, Dots[0], Dots[1])

    def fillDotsPol(self, idx: int):
        if idx == len(self.fillDots):
            return
        self.fillDotsCanvas.append(printDot(self.canvas, self.fillDots[idx],
                                            c='orange'))
        self.root.after(500, lambda: self.fillDotsPol(idx + 1))

    def completion(self):
        verts = self.polygon.vertices
        while len(self.stackInsideDots):
            dot: Dot = self.stackInsideDots.pop()
            xMin = dot.copy()
            while not checkerDotInList(verts, xMin) and \
                    not checkerDotInList(self.polygon.borderDots, xMin):
                print(len(self.stackInsideDots))
                print(xMin.x, xMin.y)
                xMin.x -= CELL_SIZE
            xMax = dot.copy()
            while not checkerDotInList(verts, xMax) and \
                    not checkerDotInList(self.polygon.borderDots, xMax):
                print(len(self.stackInsideDots))
                print(xMax.x, xMax.y)
                xMax.x += CELL_SIZE
            for x in range(xMin.x + CELL_SIZE, xMax.x, CELL_SIZE):
                self.fillDots.append(Dot(x, dot.y))
            flag = True
            for x in range(xMin.x + CELL_SIZE, xMax.x, CELL_SIZE):
                if not checkerDotInList(verts, Dot(x, dot.y - CELL_SIZE)) and \
                        not checkerDotInList(self.fillDots,
                                             Dot(x, dot.y - CELL_SIZE)) and \
                        not checkerDotInList(self.polygon.borderDots,
                                             Dot(x, dot.y - CELL_SIZE)):
                    if flag:
                        self.stackInsideDots.append(Dot(x, dot.y - CELL_SIZE))
                        flag = False
                else:
                    flag = True
            flag = True
            for x in range(xMin.x + CELL_SIZE, xMax.x, CELL_SIZE):
                if not checkerDotInList(verts, Dot(x, dot.y + CELL_SIZE)) and \
                        not checkerDotInList(self.fillDots,
                                             Dot(x, dot.y + CELL_SIZE)) and \
                        not checkerDotInList(self.polygon.borderDots,
                                             Dot(x, dot.y + CELL_SIZE)):
                    if flag:
                        self.stackInsideDots.append(Dot(x, dot.y + CELL_SIZE))
                        flag = False
                else:
                    flag = True
        self.fillDotsPol(idx=0)

    def deleteAll(self):
        self.polygon.clearPolygon()
        for elem in self.lines:
            self.canvas.delete(elem)
        self.lines.clear()
        self.stackInsideDots.clear()
        self.fillDots.clear()
        for elem in self.fillDotsCanvas:
            self.canvas.delete(elem)
        self.fillDotsCanvas.clear()
