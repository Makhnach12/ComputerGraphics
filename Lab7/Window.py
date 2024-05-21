import math
import tkinter as tk

from Lab1.launchPY.mainFunctions import getAngle, analyzeTriangle
from Lab2.Parameters import WIDTH, HEIGHT, MIDDLE
from Lab2.Root import drawGrid, drawAxes, CELL_SIZE
from Lab2.dot import Dot
from Lab3.Line import Line
from Lab4.Window import printDot, EPS
from functools import cmp_to_key

from Lab7.Triangle import Triangle

SIGNS = {'>=': lambda elem: elem[0] >= elem[1],
         '<=': lambda elem: elem[0] <= elem[1]}


def checkTriangles(tr1: Triangle, tr2: Triangle) -> bool:
    angles1: list[float] = [getAngle(
        tr1.Nodes[i],
        tr1.Nodes[(i + 1) % len(tr1.Nodes)],
        tr1.Nodes[(i + 2) % len(tr1.Nodes)]
    ) for i in range(0, len(tr1.Nodes))]
    angles2: list[float] = [getAngle(
        tr2.Nodes[i],
        tr2.Nodes[(i + 1) % len(tr2.Nodes)],
        tr2.Nodes[(i + 2) % len(tr2.Nodes)]
    ) for i in range(0, len(tr2.Nodes))]
    min1 = min(angles1)
    min2 = min(angles2)
    return min1 > min2


def checkDelone(p1: Dot, p2: Dot, p3: Dot, p0: Dot) -> bool:
    hull = bruteHull([p0, p1, p2, p3])
    if len(hull) == 3 and p0 not in hull:
        return False
    return True


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


def sortByHour(dots: list[Dot]):
    middle = Dot(0, 0)

    def comparatorDots(dot1: Dot, dot2: Dot):
        """Sorting by the hour"""
        angle1 = (math.atan2(*(dot1 - middle).coorsNorm)) * 180 / 3.14
        angle2 = (math.atan2(*(dot2 - middle).coorsNorm)) * 180 / 3.14
        if angle1 - angle2 > 0:
            return 1
        elif angle1 - angle2 < 0:
            return -1
        else:
            return 0

    for dot in dots:
        middle += dot
    middle /= len(dots)
    newDots = sorted(dots, key=cmp_to_key(comparatorDots))
    return newDots


def bruteHull(dots: list[Dot], polygonLines: list[dict] = None) -> list[Dot]:
    middle = Dot(0, 0)

    def comparatorDots(dot1: Dot, dot2: Dot):
        """Sorting by the hour"""
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
                if polygonLines is not None:
                    polygonLines.append(
                        {'stDot': dots[i],
                         'finDot': dots[j],
                         'color': 'white'}
                    )
    middle /= len(borderDots)
    borderDots = sorted(borderDots, key=cmp_to_key(comparatorDots))
    return borderDots


def checkAngle(a: Dot, b: Dot) -> bool:
    vectorComp: float = a.x * b.y - a.y * b.x
    if vectorComp < 0:
        return False
    else:
        return True


def isLine(arr: list[Dot]) -> bool:
    setX: set = set()
    setY: set = set()
    for elem in arr:
        setX.add(elem.x)
        setY.add(elem.y)
    return len(setY) == 1 or len(setX) == 1


class WindowTriangulation:
    def __init__(self):
        self.triangles = []
        self.dots = []
        self.Lines = []
        self.interLines = []
        self.dotsCanvas = []
        self.root = tk.Tk()
        self.root.title("LAB7")
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
                dot = Dot(xCell * CELL_SIZE, yCell * CELL_SIZE)
                if dot not in self.dots:
                    self.dots.append(dot)
                    self.dotsCanvas.append(
                        printDot(self.canvas, self.dots[-1], c='blue')
                    )

        self.canvas.bind('<Button-1>', click)

        tk.Button(self.root, text='алгоритм', command=self.startDivide).place(
            x=WIDTH + 90,
            y=HEIGHT // 10 + 149
        )

    def __printTriangle(self, dots: list) -> None:
        for i in range(0, len(dots)):
            self.interLines.append({'stDot': dots[i],
                                    'finDot': dots[(i + 1) % len(dots)],
                                    'color': 'yellow'})

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

    def createMergeTriangulation(self, leftFigure: list[Dot],
                                 rightFigure: list[Dot],
                                 upRibIdx: tuple[int, int],
                                 downRibIdx: tuple[int, int]) -> None:
        idxLeft, idxRight = upRibIdx
        # TODO: проверка на то что левая и правая фигуры это прямые тогда
        # просто соеднияем их
        isFirstIter: bool = False
        self.interLines.append({'stDot': rightFigure[idxRight],
                                'finDot': leftFigure[idxLeft],
                                'color': 'yellow'})
        while idxLeft != downRibIdx[0] or idxRight != downRibIdx[1]:
            # если одна из точек достигла конца то просто двигаем вторую
            # но не на первой итерации
            idxLeftNext = (idxLeft + 1) % len(leftFigure)
            idxRightNext = (idxRight - 1) % len(rightFigure)

            if isFirstIter:
                if idxLeft == downRibIdx[0]:
                    self.interLines.append({'stDot': rightFigure[idxRightNext],
                                            'finDot': leftFigure[idxLeft],
                                            'color': 'yellow'})
                    idxRight = idxRightNext
                    continue
                elif idxRight == downRibIdx[1]:
                    self.interLines.append({'stDot': leftFigure[idxLeftNext],
                                            'finDot': rightFigure[idxRight],
                                            'color': 'yellow'})
                    idxLeft = idxLeftNext
                    continue

            angle: tuple[Dot, Dot] = (
                leftFigure[idxLeft] - rightFigure[idxRight],
                rightFigure[idxRightNext] - rightFigure[idxRight]
            )
            #TODO: сделать проверку для всех пограничных точек
            if checkAngle(*angle) and checkDelone(rightFigure[idxRightNext],
                                                  leftFigure[idxLeft],
                                                  rightFigure[idxRight],
                                                  leftFigure[idxLeftNext]) \
                    and checkDelone(rightFigure[idxRightNext],
                                    leftFigure[idxLeft],
                                    rightFigure[idxRight],
                                    leftFigure[(idxLeftNext + 1) %
                                               len(leftFigure)]):
                self.interLines.append({'stDot': rightFigure[idxRightNext],
                                        'finDot': leftFigure[idxLeft],
                                        'color': 'yellow'})
                idxRight = idxRightNext
            else:
                self.interLines.append({'stDot': rightFigure[idxRight],
                                        'finDot': leftFigure[idxLeftNext],
                                        'color': 'yellow'})
                idxLeft = idxLeftNext
            isFirstIter = True

    def mergerHull(self, leftFigure, rightFigure):
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
                        orientation(rightFigure[downRight],
                                    leftFigure[downLeft],
                                    leftFigure[i % len(leftFigure)]) == 0:
                    newFigure.append(leftFigure[i % len(leftFigure)])
                    i += 1
            else:
                newFigure.append(leftFigure[upperLeft])
        self.interLines.append({'stDot': leftFigure[downLeft],
                                'finDot': rightFigure[downRight],
                                'color': 'red'})
        self.createMergeTriangulation(leftFigure, rightFigure,
                                      (upperLeft, upperRight),
                                      (downLeft, downRight))
        return sortByHour(newFigure)

    def divide(self, dots):
        if len(dots) == 3:
            self.triangles.append(Triangle(*dots))
            self.__printTriangle(dots)
            return bruteHull(dots)
        elif len(dots) == 4:
            convexHull: list[Dot] = bruteHull(dots, self.interLines)
            if len(convexHull) == 3:
                centerDot: Dot = [dot for dot in dots if dot not in
                                  convexHull][0]
                for i in range(0, len(convexHull)):
                    self.__printTriangle([centerDot,
                                          convexHull[i % len(convexHull)],
                                          convexHull[
                                              (i + 1) % len(convexHull)]])
            else:
                if not checkDelone(*dots):
                    self.__printTriangle([convexHull[0], convexHull[1],
                                          convexHull[2]])
                    self.__printTriangle([convexHull[2], convexHull[3],
                                          convexHull[0]])
                else:
                    self.__printTriangle([convexHull[0], convexHull[1],
                                          convexHull[3]])
                    self.__printTriangle([convexHull[1], convexHull[3],
                                          convexHull[2]])
            return bruteHull(dots)
        elif len(dots) == 5:
            dots.append(dots[-1])
            start = len(dots) // 2
            left, right = [dots[i] for i in range(start)], \
                [dots[i] for i in range(start, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            return newFigure
        elif len(dots) == 8:
            start = len(dots) // 2
            left, right = [dots[i] for i in range(start)], \
                [dots[i] for i in range(start, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            return newFigure
        # TODO: если точек пять то дублируем одну
        elif len(dots) < 12:
            left, right = [dots[i] for i in range(3)], \
                [dots[i] for i in range(3, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            return newFigure
        else:
            start = len(dots) // 2
            left, right = [dots[i] for i in range(start)], \
                [dots[i] for i in range(start, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            return newFigure

    def startDivide(self):
        def comparatorDots(dot1: Dot, dot2: Dot):
            if dot1.x - dot2.x > 0:
                return 1
            elif dot1.x - dot2.x < 0:
                return -1
            else:
                if dot1.y - dot2.y > 0:
                    return -1
                elif dot1.y - dot2.y < 0:
                    return 1
            return 0

        self.dots = sorted(self.dots, key=cmp_to_key(comparatorDots))
        self.divide(self.dots)
        self.animLine(0)
