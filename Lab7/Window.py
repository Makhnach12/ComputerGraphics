import math
import tkinter as tk

from Lab1.launchPY.mainFunctions import getAngle
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


def sinA(a: Dot, b: Dot, c: Dot):
    dots = bruteHull([a, b, c])
    midDotInd = dots.index(b)
    newB, newC, newA = dots[midDotInd], dots[(midDotInd + 1) % len(dots)], \
        dots[(midDotInd + 2) % len(dots)]
    vectorBA: Dot = newA - newB
    vectorBC: Dot = newC - newB
    vectorComp: float = vectorBA.x * vectorBC.y - vectorBA.y * vectorBC.x
    return vectorComp / (math.sqrt(vectorBA.x ** 2 + vectorBA.y ** 2) *
                         math.sqrt(vectorBC.x ** 2 + vectorBC.y ** 2))


def checkDelone(p1: Dot, p2: Dot, p3: Dot, p0: Dot) -> bool:
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

    for elem in [p0, p1, p2, p3]:
        middle += elem
    middle /= 4
    polygon = sorted([p0, p1, p2, p3], key=cmp_to_key(comparatorDots))
    # s_a = (p0.x - p1.x) * (p0.x - p3.x) + (p0.y - p1.y) * (p0.y - p3.y)
    # s_b = (p2.x - p1.x) * (p2.x - p3.x) + (p2.y - p1.y) * (p2.y - p3.y)
    # if s_a < 0 and s_b < 0:
    #     return False
    # elif s_a >= 0 and s_b >= 0:
    #     return True
    hull = bruteHull([p0, p1, p2, p3])
    if len(hull) == 3 and p0 not in hull:
        return False
    midDotIndA = polygon.index(p0)
    angleA = [polygon[(midDotIndA - 1) % len(polygon)], polygon[midDotIndA],
              polygon[(midDotIndA + 1) % len(polygon)]]
    sin_a = sinA(*angleA)
    angleRadA = math.asin(sin_a)
    # if (angleA[1].x - angleA[0].x) * (angleA[1].x - angleA[2].x) + \
    #     (angleA[1].y - angleA[0].y) * (angleA[1].y - angleA[2].y) < 0:
    #     angleRadA += math.pi / 2
    # cos_a = sqrt(1 - sin_a * sin_a)
    midDotIndB = polygon.index([elem for elem in polygon
                                if elem not in angleA][0])
    angleB = [polygon[(midDotIndB - 1) % len(polygon)], polygon[midDotIndB],
              polygon[(midDotIndB + 1) % len(polygon)]]
    sin_b = sinA(*angleB)
    angleRadB = math.asin(sin_b)
    # if (angleB[1].x - angleB[0].x) * (angleB[1].x - angleB[2].x) + \
    #     (angleB[1].y - angleB[0].y) * (angleB[1].y - angleB[2].y) < 0:
    #     angleRadB += math.pi / 2
    # cos_b = sqrt(1 - sin_b * sin_b)
    return angleRadA + angleRadB - math.pi < 0


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


def findAdjacentTriangles(triangles: list[Triangle], triangle: Triangle):
    for elem in triangles:
        elem.addNeighbor(triangle)
        triangle.addNeighbor(elem)


def addNeighbors(tr1: Triangle, tr2: Triangle):
    tr1.addNeighbor(tr2)
    tr2.addNeighbor(tr1)


def swap(tr1: Triangle, tr2: Triangle):
    boundDots: list[Dot] = [dot for dot in tr1.Nodes if dot not in tr2.Nodes]
    boundDots += [dot for dot in tr2.Nodes if dot not in tr1.Nodes]
    rib = [dot for dot in tr1.Nodes if dot not in boundDots]
    newTr1 = Triangle(boundDots[0], boundDots[1], rib[0])
    newTr2 = Triangle(boundDots[0], boundDots[1], rib[1])
    addNeighbors(newTr1, newTr2)
    for elem1, elem2 in zip(tr1.neighborTriangles.values(),
                            tr2.neighborTriangles.values()):
        if elem1 is tr2 or elem2 is tr1:
            continue
        newTr1.addNeighbor(elem1, elem2)
        newTr2.addNeighbor(elem1, elem2)
    return newTr1, newTr2


def stableTriangle(triangle: Triangle):
    isGood = False
    while not isGood:
        print('Цикл', 1)
        isGood = True
        for tr in triangle.neighborTriangles.values():
            polygon = [elem for elem in triangle.Nodes]
            polygon += [elem for elem in tr.Nodes if elem not in triangle.Nodes]
            if len(polygon) == 3:
                return
            if not checkDelone(*polygon):
                isGood = False
                triangle, tr = swap(triangle, tr)
                break


def checkAngle(a: Dot, b: Dot, c: Dot) -> bool:
    vectorBA: Dot = a - b
    vectorBC: Dot = c - b
    vectorComp: float = vectorBA.x * vectorBC.y - vectorBA.y * vectorBC.x
    if vectorComp <= 0:
        return False
    else:
        return True


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

    def createMergeTriangulation(self, leftFigure: list[Dot],
                                 rightFigure: list[Dot],
                                 upRibIdx: tuple[int, int],
                                 downRibIdx: tuple[int]) -> None:
        idxLeft, idxRight = upRibIdx
        while idxLeft % len(leftFigure) != downRibIdx[0] or \
                idxRight % len(rightFigure) != downRibIdx[1]:
            print('Цикл', 2)
            print(idxLeft, idxRight, downRibIdx)
            tr1: Triangle = Triangle(*bruteHull(
                [rightFigure[idxRight],
                 leftFigure[idxLeft],
                 leftFigure[(idxLeft + 1) % len(leftFigure)]]
            ))
            tr2: Triangle = Triangle(*bruteHull([leftFigure[idxLeft],
                                                 rightFigure[
                                                     (idxRight - 1) % len(
                                                         rightFigure)],
                                                 rightFigure[idxRight]]))
            angleTr1: bool = checkAngle(leftFigure[idxLeft],
                                        rightFigure[idxRight],
                                        leftFigure
                                        [
                                            (idxLeft + 1) % len(leftFigure)
                                            ])
            angleTr2: bool = checkAngle(rightFigure
                                        [
                                            (idxRight - 1) % len(rightFigure)
                                            ],
                                        leftFigure[idxLeft],
                                        rightFigure[idxRight])
            print(angleTr1, checkDelone(*tr1.Nodes, rightFigure[(idxRight - 1)
                                                                % len(
                rightFigure)]))
            print(angleTr2, checkDelone(*tr2.Nodes, leftFigure[(idxLeft + 1)
                                                               % len(
                leftFigure)]))
            if angleTr1 and checkDelone(*tr1.Nodes,
                                        rightFigure[
                                            (idxRight - 1) % len(rightFigure)]) \
                    and idxLeft != downRibIdx[0]:
                findAdjacentTriangles(self.triangles, tr1)
                self.triangles.append(tr1)
                stableTriangle(tr1)
                idxLeft = (idxLeft + 1) % len(leftFigure)
            else:
                findAdjacentTriangles(self.triangles, tr2)
                self.triangles.append(tr2)
                stableTriangle(tr2)
                idxRight = (idxRight - 1) % len(rightFigure)
                # if idxRight == -1:
                #     idxRight = len(rightFigure) - 1

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
            print(3)
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
            print(5)
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
            print(6)
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
        return newFigure

    def divide(self, dots):
        if len(dots) == 3:
            self.triangles.append(Triangle(*dots))
            for elem in self.triangles:
                elem.drawTriangle(self.canvas)
            return bruteHull(dots)
        elif len(dots) == 4:
            convexHull: list[Dot] = bruteHull(dots, self.interLines)
            if len(convexHull) == 3:
                centerDot: Dot = [dot for dot in dots if dot not in
                                  convexHull][0]
                triangles = [Triangle(centerDot,
                                      convexHull[i % len(convexHull)],
                                      convexHull[(i + 1) % len(convexHull)])
                             for i in range(0, len(convexHull))]
                for elem in triangles:
                    elem.addNeighbor(*[tr for tr in triangles if tr is not
                                       elem])
                self.triangles += triangles
            else:
                if not checkDelone(*dots):
                    triangles = [Triangle(convexHull[0], convexHull[1],
                                          convexHull[2]),
                                 Triangle(convexHull[2], convexHull[3],
                                          convexHull[0])]
                else:
                    triangles = [Triangle(convexHull[0], convexHull[1],
                                          convexHull[3]),
                                 Triangle(convexHull[1], convexHull[3],
                                          convexHull[2])]
                triangles[0].addNeighbor(triangles[1])
                triangles[1].addNeighbor(triangles[0])
                self.triangles += triangles
            for elem in self.triangles:
                elem.drawTriangle(self.canvas)
            return bruteHull(dots)
        elif len(dots) == 8:
            print('Yes8')
            start = len(dots) // 2
            left, right = [dots[i] for i in range(start)], \
                [dots[i] for i in range(start, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            for elem in self.triangles:
                elem.drawTriangle(self.canvas)
            return newFigure
        elif len(dots) < 12:
            print('Yes<12')
            left, right = [dots[i] for i in range(3)], \
                [dots[i] for i in range(3, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            for elem in self.triangles:
                elem.drawTriangle(self.canvas)
            return newFigure
        else:
            print('Yes>12')
            start = len(dots) // 2
            left, right = [dots[i] for i in range(start)], \
                [dots[i] for i in range(start, len(dots))]
            left_hull, right_hull = self.divide(left), self.divide(right)
            newFigure: list[Dot] = self.mergerHull(left_hull, right_hull)
            for elem in self.triangles:
                elem.drawTriangle(self.canvas)
            return newFigure

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
        self.divide(self.dots)
        # for i in range(len(finalFig) - 1):
        #     self.interLines.append({'stDot': finalFig[i],
        #                             'finDot': finalFig[i + 1],
        #                             'color': 'yellow'})
        # else:
        #     self.interLines.append({'stDot': finalFig[-1],
        #                             'finDot': finalFig[0],
        #                             'color': 'yellow'})
