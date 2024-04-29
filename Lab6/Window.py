import math
import tkinter as tk

from Lab2.Parameters import WIDTH, HEIGHT, MIDDLE
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab3.Line import Line
from Lab4.Window import printDot, EPS
from functools import cmp_to_key

SIGNS = {'>=': lambda elem: elem[0] >= elem[1],
         '<=': lambda elem: elem[0] <= elem[1]}


def orientationAllDots(a: Dot, b: Dot, arr: list, sign):
    for elem in arr:
        if not SIGNS[sign]([orientation(a, b, elem), 0]):
            return False
    return True


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
        self.Lines = []
        self.interLines = []
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
                if Dot(xCell * CELL_SIZE, yCell * CELL_SIZE) not in self.dots:
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
                    self.interLines.append({'stDot': dots[i],
                                            'finDot': dots[j],
                                            'color': 'white'})
        middle /= len(borderDots)
        borderDots = sorted(borderDots, key=cmp_to_key(comparatorDots))
        return borderDots

    def animLine(self, idx: int):
        if idx == len(self.interLines):
            for i in range(len(self.interLines)):
                if self.interLines[i]['color'] != 'yellow':
                    self.canvas.delete(self.Lines[i])
            return
        if idx - 1 >= 0 and self.interLines[idx - 1]['color'] == 'green':
            self.canvas.delete(self.Lines[idx - 1])
        self.Lines.append(self.canvas.create_line(
            self.interLines[idx]['stDot'].coors,
            self.interLines[idx]['finDot'].coors,
            fill=self.interLines[idx]['color'], width=2))
        self.root.after(500, lambda: self.animLine(idx + 1))

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
        self.interLines.append({'stDot': leftFigure[upperLeft],
                                'finDot': rightFigure[upperRight],
                                'color': 'green'})
        while not done:
            done = True
            while not orientationAllDots(rightFigure[upperRight],
                                         leftFigure[upperLeft], leftFigure,
                                         '<='):
                upperLeft = (upperLeft - 1) % lenLeft
                self.interLines.append({'stDot': leftFigure[upperLeft],
                                        'finDot': rightFigure[upperRight],
                                        'color': 'green'})
            while not orientationAllDots(leftFigure[upperLeft],
                                         rightFigure[upperRight],
                                         rightFigure, '>='):
                upperRight = (upperRight + 1) % lenRight
                self.interLines.append({'stDot': leftFigure[upperLeft],
                                        'finDot': rightFigure[upperRight],
                                        'color': 'green'})
                done = False
        downLeft, downRight = idxLeft, idxRight
        self.interLines.append({'stDot': leftFigure[upperLeft],
                                'finDot': rightFigure[upperRight],
                                'color': 'red'})
        done = False
        while not done:
            done = True
            while not orientationAllDots(rightFigure[downRight],
                                         leftFigure[downLeft],
                                         leftFigure, '>='):
                downLeft = (downLeft + 1) % lenLeft
                self.interLines.append({'stDot': leftFigure[downLeft],
                                        'finDot': rightFigure[downRight],
                                        'color': 'green'})
            while not orientationAllDots(leftFigure[downLeft],
                                         rightFigure[downRight],
                                         rightFigure, '<='):
                downRight = (downRight - 1) % lenRight
                self.interLines.append({'stDot': leftFigure[downLeft],
                                        'finDot': rightFigure[downRight],
                                        'color': 'green'})
                done = False
        newFigure = []
        i = upperRight
        while i % len(rightFigure) != downRight:
            newFigure.append(rightFigure[i % len(rightFigure)])
            i += 1
        else:
            if upperRight % len(rightFigure) == downRight:
                newFigure.append(rightFigure[i % len(rightFigure)])
                i += 1
                while i % len(rightFigure) != downRight and \
                        orientation(leftFigure[upperLeft],
                                    rightFigure[upperRight],
                                    rightFigure[i % len(rightFigure)]) == 0:
                    newFigure.append(rightFigure[i % len(rightFigure)])
                    i += 1
            else:
                newFigure.append(rightFigure[downRight])

        i = downLeft
        while i % len(leftFigure) != upperLeft:
            newFigure.append(leftFigure[i % len(leftFigure)])
            i += 1
        else:
            if downLeft % len(leftFigure) == upperLeft:
                newFigure.append(leftFigure[i % len(leftFigure)])
                i += 1
                while i % len(leftFigure) != upperLeft and \
                        orientation(rightFigure[downRight], leftFigure[downLeft],
                                    leftFigure[i % len(leftFigure)]) == 0:
                    newFigure.append(leftFigure[i % len(leftFigure)])
                    i += 1
            else:
                newFigure.append(leftFigure[upperLeft])
        self.interLines.append({'stDot': leftFigure[downLeft],
                                'finDot': rightFigure[downRight],
                                'color': 'red'})
        return newFigure

    def divide(self, dots):
        if len(dots) <= 3:
            return self.bruteHull(dots)
        start = len(dots) // 2
        left, right = [dots[i] for i in range(start)], \
            [dots[i] for i in range(start, len(dots))]
        left_hull, right_hull = self.divide(left), self.divide(right)
        return self.merger(left_hull, right_hull)

    def startDivide(self):
        def comparatorDots(dot1: Dot, dot2: Dot):
            if dot1.x - dot2.x > 0:
                return 1
            elif dot1.x - dot2.x < 0:
                return -1
            else:
                if dot1.y - dot2.y > 0:
                    return 1
                elif dot1.y - dot2.y < 0:
                    return -1
                return 0

        self.dots = sorted(self.dots, key=cmp_to_key(comparatorDots))
        finalFig = self.divide(self.dots)
        for i in range(len(finalFig) - 1):
            self.interLines.append({'stDot': finalFig[i],
                                    'finDot': finalFig[i + 1],
                                    'color': 'yellow'})
        else:
            self.interLines.append({'stDot': finalFig[-1],
                                    'finDot': finalFig[0],
                                    'color': 'yellow'})
        self.animLine(0)

    def deleteAll(self):
        for elem in self.dotsCanvas:
            self.canvas.delete(elem)
        for elem in self.Lines:
            self.canvas.delete(elem)
        self.dotsCanvas.clear()
        self.dots.clear()
        self.Lines.clear()
        self.interLines.clear()
