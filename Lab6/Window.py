import math
import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT, MIDDLE
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab3.Line import Line
from Lab4.Window import printDot, EPS
from functools import cmp_to_key


def orientation(a: Dot, b: Dot, c: Dot):
    res = (b.y - a.y) * (c.x - b.x) - (c.y - b.y) * (b.x - a.x)
    if res == 0:
        return 0
    if res > 0:
        return 1
    return -1


class WindowHullMethod:
    def __init__(self):
        self.dots = []
        self.borderDots = []
        self.dotsCanvas = []
        self.root = tk.Tk()
        self.root.title("LAB6")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.canvas.pack(side=tk.LEFT)

        def click(event):
            x, y = event.x, event.y
            if not 0 <= x < WIDTH or not 0 <= y < HEIGHT:
                return
            normX, normY = x - MIDDLE[0], MIDDLE[1] - y
            xCell, yCell = normX // CELL_SIZE, normY // CELL_SIZE
            if abs(abs(normX / CELL_SIZE) - abs(xCell)) > 0.5:
                xCell += 1
            if abs(abs(normY / CELL_SIZE) - abs(yCell)) > 0.5:
                yCell += 1
            if abs(abs(normX // CELL_SIZE) - abs(normX / CELL_SIZE)) < EPS:
                self.dots.append(Dot(xCell * CELL_SIZE, yCell * CELL_SIZE))
                self.dotsCanvas.append(
                    printDot(self.canvas, self.dots[-1], c='blue')
                )

        self.canvas.bind('<Button-1>', click)
        tk.Button(self.root, text='Сброс', command=self.deleteAll).place(
            x=WIDTH + 90,
            y=HEIGHT // 10 + 100
        )

        tk.Button(self.root, text='алгоритм', command=self.startDivide).place(
            x=WIDTH + 90,
            y=HEIGHT // 10 + 149
        )

    def bruteHull(self, dots: list[Dot]):
        middle = Dot(0, 0)

        def comparatorDots(dot1: Dot, dot2: Dot):
            angle1 = (math.atan2(*(dot1 - middle).coorsNorm)) * 180 / 3.14
            angle2 = (math.atan2(*(dot2 - middle).coorsNorm)) * 180 / 3.14
            if angle1 - angle2 > 0:
                return 1
            elif angle1 - angle2 < 0:
                return -1
            else:
                return 0

        borderDots = []
        for i in range(len(dots)):
            for j in range(i + 1, len(dots)):
                ln = Line()
                ln.createLine(dots[i], dots[j])
                a, b, c = ln.getLineCoef()
                pos, neg = 0, 0
                for k in range(len(dots)):
                    if (k == i) or (k == j) or (
                            a * dots[k].x + b * dots[k].y + c <= 0):
                        neg += 1
                    if (k == i) or (k == j) or (
                            a * dots[k].x + b * dots[k].y + c >= 0):
                        pos += 1
                if pos == len(dots) or neg == len(dots):
                    if dots[i] not in borderDots:
                        middle += dots[i]
                        borderDots.append(dots[i])
                    if dots[j] not in borderDots:
                        middle += dots[j]
                        borderDots.append(dots[j])
                    self.canvas.create_line(dots[i].coors,
                                            dots[j].coors,
                                            width=2)
        middle /= len(borderDots)
        borderDots = sorted(borderDots, key=cmp_to_key(comparatorDots))
        return borderDots

    def merger(self, leftFigure, rightFigure):
        idxLeft, idxRight = 0, 0
        for i in range(0, len(leftFigure)):
            if leftFigure[i].x > leftFigure[idxLeft].x:
                idxLeft = i
        for i in range(0, len(rightFigure)):
            if rightFigure[i].x < rightFigure[idxRight].x:
                idxRight = i

        lenLeft, lenRight = len(leftFigure), len(rightFigure)
        upperLeft, upperRight = idxLeft, idxRight
        done = False
        while not done:
            done = True
            while orientation(rightFigure[upperRight],
                              leftFigure[upperLeft],
                              leftFigure[(upperLeft - 1) % lenLeft]) >= 0:
                upperLeft = (upperLeft - 1) % lenLeft
            while orientation(leftFigure[upperLeft], rightFigure[upperRight],
                              rightFigure[(upperRight + 1) % lenRight]) <= 0:
                upperRight = (upperRight + 1) % lenRight
                done = False
        downLeft, downRight = idxLeft, idxRight
        done = False
        while not done:
            done = True
            while orientation(rightFigure[downRight],
                              leftFigure[downLeft],
                              leftFigure[(downLeft + 1) % lenLeft]) <= 0:
                downLeft = (downLeft + 1) % lenLeft
            while orientation(leftFigure[downLeft], rightFigure[downRight],
                              rightFigure[(downRight - 1) % lenRight]) >= 0:
                downRight = (downRight - 1) % lenRight
                done = False
        newFigure = []
        i = upperRight
        while i % len(rightFigure) != downRight:
            newFigure.append(rightFigure[i % len(rightFigure)])
            i += 1
        else:
            newFigure.append(rightFigure[downRight])
        i = downLeft
        while i % len(leftFigure) != upperLeft:
            newFigure.append(leftFigure[i % len(leftFigure)])
            i += 1
        else:
            newFigure.append(leftFigure[upperLeft])
        self.canvas.create_line(leftFigure[upperLeft].coors,
                                rightFigure[upperRight].coors,
                                width=2, fill='red')
        self.canvas.create_line(leftFigure[downLeft].coors,
                                rightFigure[downRight].coors,
                                width=2, fill='red')
        print('Длина фигуры', len(newFigure))
        for elem in newFigure:
            print(elem)
        return newFigure

    def divide(self, dots):
        if len(dots) <= 5:
            return self.bruteHull(dots)
        left, right = [], []
        start = int(len(dots) / 2)
        for i in range(start):
            left.append(dots[i])
        for i in range(start, len(dots)):
            right.append(dots[i])
        left_hull = self.divide(left)
        right_hull = self.divide(right)
        return self.merger(left_hull, right_hull)

    def startDivide(self):
        def comparatorDots(dot1: Dot, dot2: Dot):
            if dot1.x - dot2.x > 0:
                return 1
            elif dot1.x - dot2.x < 0:
                return -1
            else:
                return 0

        self.dots = sorted(self.dots, key=cmp_to_key(comparatorDots))
        self.divide(self.dots)

    def deleteAll(self):
        for elem in self.dotsCanvas:
            self.canvas.delete(elem)
        self.dotsCanvas.clear()
        self.dots.clear()
