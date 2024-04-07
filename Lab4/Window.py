import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab3.Line import Line, RAD
from Lab3.Window import cleanEntry
from Lab4.Polygon import Rectangle

INSIDE = 0b0000
LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100
TOP = 0b1000


def printDot(canvas, dot: Dot):
    return canvas.create_oval(dot.coors[0] - RAD, dot.coors[1] - RAD,
                              dot.coors[0] + RAD, dot.coors[1] + RAD,
                              fill='blue')


def computeCode(dot: Dot, coorsRect):
    code = INSIDE
    if dot.x < coorsRect[0]:
        code |= LEFT
    elif dot.x > coorsRect[2]:
        code |= RIGHT
    if dot.y < coorsRect[3]:
        code |= BOTTOM
    elif dot.y > coorsRect[1]:
        code |= TOP
    return code


class WindowSutherland_Cohen:
    def __init__(self):
        self.intersecPoints = []
        self.intersecPointsCanvas = []
        self.polygon = None
        self.root = tk.Tk()
        self.root.title("LAB4_1.COM")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.line = Line(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.canvas.pack(side=tk.LEFT)

        label_above_button = tk.Label(self.root, text="Координаты верхнего "
                                                      "левого угла")
        label_above_button.place(x=WIDTH + 20, y=HEIGHT // 10 - 30)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 10)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 30, y=HEIGHT // 10 + 10)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 - 10)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 130, y=HEIGHT // 10 + 10)

        label_above_button = tk.Label(self.root, text="Координаты правого "
                                                      "нижнего угла")
        label_above_button.place(x=WIDTH + 20, y=HEIGHT // 10 + 40)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 + 60)

        entryX2 = tk.Entry(self.root, width=10)
        entryX2.place(x=WIDTH + 30, y=HEIGHT // 10 + 80)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 + 60)

        entryY2 = tk.Entry(self.root, width=10)
        entryY2.place(x=WIDTH + 130, y=HEIGHT // 10 + 80)
        createLineButton = tk.Button(self.root, text='Задать прямоугольник',
                                     command=lambda: self.addPolygon(
                                         Rectangle,
                                         [
                                             Dot(int(entryX.get()) * CELL_SIZE,
                                                 int(entryY.get()) * CELL_SIZE),
                                             Dot(int(entryX2.get()) * CELL_SIZE,
                                                 int(entryY2.get()) * CELL_SIZE)
                                         ]
                                     )
                                     )
        cleanEntry([entryX, entryY2, entryX2, entryY])
        createLineButton.place(x=WIDTH + 40, y=HEIGHT // 10 + 110)

        label_above_button = tk.Label(self.root, text="Координаты начала")
        label_above_button.place(x=WIDTH + 60, y=HEIGHT // 10 + 150)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 + 180)

        entryXLine = tk.Entry(self.root, width=10)
        entryXLine.place(x=WIDTH + 30, y=HEIGHT // 10 + 210)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 + 180)

        entryYLine = tk.Entry(self.root, width=10)
        entryYLine.place(x=WIDTH + 130, y=HEIGHT // 10 + 210)

        label_above_button = tk.Label(self.root, text="Координаты конца")
        label_above_button.place(x=WIDTH + 60, y=HEIGHT // 10 + 240)

        tk.Label(self.root, text="Координата x:").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 + 240)

        entryX2Line = tk.Entry(self.root, width=10)
        entryX2Line.place(x=WIDTH + 30, y=HEIGHT // 10 + 270)

        tk.Label(self.root, text="Координата y:").place(x=WIDTH + 130,
                                                        y=HEIGHT // 10 + 240)

        entryY2Line = tk.Entry(self.root, width=10)
        entryY2Line.place(x=WIDTH + 130, y=HEIGHT // 10 + 270)
        createLineButton = tk.Button(self.root, text='Задать прямую',
                                     command=lambda: self.line.createLine(
                                         Dot(int(entryXLine.get()) * CELL_SIZE,
                                             int(entryYLine.get()) * CELL_SIZE),
                                         Dot(int(entryX2Line.get()) * CELL_SIZE,
                                             int(entryY2Line.get()) * CELL_SIZE)
                                     ))
        cleanEntry([entryXLine, entryY2Line, entryX2Line, entryYLine])
        createLineButton.place(x=WIDTH + 70, y=HEIGHT // 10 + 300)

        tk.Button(self.root, text='Выделить точки ограничения',
                  command=self.Sutherland_Cohen).place(x=WIDTH + 30,
                                                       y=HEIGHT // 10 + 330)
        tk.Button(self.root, text='Сброс',
                  command=self.deleteAll).place(x=WIDTH + 100,
                                                y=HEIGHT // 10 + 360)

    def addPolygon(self, polygonType, Dots: list[Dot]):
        self.polygon = polygonType(self.canvas, Dots[0], Dots[1])

    def Sutherland_Cohen(self):
        dotsLine = self.line.dots
        x1, y1 = dotsLine[0].x, dotsLine[0].y
        x2, y2 = dotsLine[1].x, dotsLine[1].y
        code1 = computeCode(dotsLine[0], self.polygon.coors)
        code2 = computeCode(dotsLine[1], self.polygon.coors)
        accept = False
        polygonCoors = self.polygon.coors
        while True:
            if code1 == 0 and code2 == 0:
                accept = True
                break
            elif (code1 & code2) != 0:
                break
            else:
                x, y = 1, 1
                if code1 != 0b0000:
                    code_out = code1
                else:
                    code_out = code2
                if code_out & TOP:
                    x = x1 + ((x2 - x1) / (y2 - y1)) * (polygonCoors[1] - y1)
                    y = polygonCoors[1]
                elif code_out & BOTTOM:
                    x = x1 + ((x2 - x1) / (y2 - y1)) * (polygonCoors[3] - y1)
                    y = polygonCoors[3]
                elif code_out & RIGHT:
                    y = y1 + ((y2 - y1) / (x2 - x1)) * (polygonCoors[2] - x1)
                    x = polygonCoors[2]
                elif code_out & LEFT:
                    y = y1 + ((y2 - y1) / (x2 - x1)) * (polygonCoors[0] - x1)
                    x = polygonCoors[0]
                if code_out == code1:
                    x1, y1 = x, y
                    code1 = computeCode(Dot(x1, y1), self.polygon.coors)
                else:
                    x2, y2 = x, y
                    code2 = computeCode(Dot(x2, y2), self.polygon.coors)
        if accept:
            self.intersecPoints.append(Dot(x1, y1))
            self.intersecPoints.append(Dot(x2, y2))
            self.intersecPointsCanvas.append(printDot(self.canvas,
                                                      self.intersecPoints[0]))
            self.intersecPointsCanvas.append(printDot(self.canvas,
                                                      self.intersecPoints[1]))

    def deleteAll(self):
        for elem in self.intersecPointsCanvas:
            self.canvas.delete(elem)
        self.intersecPointsCanvas.clear()
        self.intersecPoints.clear()
        self.line.deleteLine()
        self.polygon.clearPolygon()
        self.polygon = None
