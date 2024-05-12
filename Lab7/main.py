# from Lab2.dot import Dot
# from Lab7.Triangle import Rib, Triangle
#
# gg = Rib(Dot(0, 0), Dot(1, 1))
# gg2 = Rib(Dot(0, 1), Dot(1, 1))
#
# a = Triangle(Dot(0, 0), Dot(0, 1), Dot(1, 0))
# b = Triangle(Dot(1, 1), Dot(2, 1), Dot(-1, 0))
# arr = [a, b]
# if a is not arr[0]:
#     print('YES')
# print(a.neighborTriangles)
import math
from math import sqrt
from functools import cmp_to_key
import numpy as np

from Lab2.dot import Dot
from Lab6.Window import bruteHull


# from Lab1.launchPY.mainFunctions import getAngle
# from Lab2.dot import Dot
# from Lab7.Window import checkAngle, checkDelone

# arr = {gg: 'gg', gg2: 'gg2'}
# print(arr[Rib(Dot(0, 1), Dot(1, 1))])

from Lab7.Window import WindowTriangulation

win = WindowTriangulation()
win.root.mainloop()
# a,b = (0,0 )
# print(a, b)
# dot1 = Dot(20, 160)
# dot2 = Dot(-80, 60)
# dot3 = Dot(-160, 160)
# dot4 = Dot(-60, 140)
# print(getAngle(dot1, dot2, dot3))
# print(checkAngle(dot1, dot2, dot3))
# print(checkDelone(dot1, dot2, dot3, dot4))
def checkAngle(a: Dot, b: Dot, c: Dot) -> bool:
    vectorBA: Dot = a - b
    vectorBC: Dot = c - b
    vectorComp: float = vectorBA.x * vectorBC.y - vectorBA.y * vectorBC.x
    if vectorComp <= 0:
        return False
    else:
        return True


def sinA(a: Dot, b: Dot, c: Dot):
    dots = bruteHull([a, b, c])
    midDotInd = dots.index(b)
    newB, newC, newA = dots[midDotInd], dots[(midDotInd + 1) % len(dots)], \
        dots[(midDotInd + 2) % len(dots)]
    vectorBA: Dot = newA - newB
    vectorBC: Dot = newC - newB
    vectorComp: float = vectorBA.x * vectorBC.y - vectorBA.y * vectorBC.x
    return vectorComp / (sqrt(vectorBA.x ** 2 + vectorBA.y ** 2) *
                         sqrt(vectorBC.x ** 2 + vectorBC.y ** 2))


def sinB(a: Dot, b: Dot, c: Dot):
    vectorBA: Dot = a - b
    vectorBC: Dot = c - b
    vectorComp: float = vectorBA.x * vectorBC.y - vectorBA.y * vectorBC.x
    return vectorComp / (sqrt(vectorBA.x ** 2 + vectorBA.y ** 2) *
                         sqrt(vectorBC.x ** 2 + vectorBC.y ** 2))


def sort_coordinates(list_of_xy_coords):
    cx, cy = list_of_xy_coords.mean(0)
    x, y = list_of_xy_coords.T
    angles = np.arctan2(x - cx, y - cy)
    indices = np.argsort(angles)
    return indices


def checkDelone1(p1: Dot, p2: Dot, p3: Dot, p0: Dot) -> bool:
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
    if (angleA[1].x - angleA[0].x) * (angleA[1].x - angleA[2].x) + \
        (angleA[1].y - angleA[0].y) * (angleA[1].y - angleA[2].y) < 0:
        angleRadA += math.pi
    # cos_a = sqrt(1 - sin_a * sin_a)
    midDotIndB = polygon.index([elem for elem in polygon
                                if elem not in angleA][0])
    angleB = [polygon[(midDotIndB - 1) % len(polygon)], polygon[midDotIndB],
              polygon[(midDotIndB + 1) % len(polygon)]]
    sin_b = sinA(*angleB)
    angleRadB = math.asin(sin_b)
    if (angleB[1].x - angleB[0].x) * (angleB[1].x - angleB[2].x) + \
        (angleB[1].y - angleB[0].y) * (angleB[1].y - angleB[2].y) < 0:
        angleRadB += math.pi
    # cos_b = sqrt(1 - sin_b * sin_b)
    return angleRadA + angleRadB - math.pi < 0


def checkDelone2(p1: Dot, p2: Dot, p3: Dot, p0: Dot) -> bool:
    s_a = (p0.x - p1.x) * (p0.x - p3.x) + (p0.y - p1.y) * (p0.y - p3.y)
    s_b = (p2.x - p1.x) * (p2.x - p3.x) + (p2.y - p1.y) * (p2.y - p3.y)
    if s_a < 0 and s_b < 0:
        return False
    elif s_a >= 0 and s_b >= 0:
        return True
    hull = bruteHull([p0, p1, p2, p3])
    if len(hull) == 3:
        return False
    midDotIndA = hull.index(p0)
    angleA = [hull[(midDotIndA - 1) % len(hull)], hull[midDotIndA],
              hull[(midDotIndA + 1) % len(hull)]]
    sin_a = sinA(*angleA)
    angleRadA = math.asin(sin_a)
    # cos_a = sqrt(1 - sin_a * sin_a)
    midDotIndB = hull.index([elem for elem in hull if elem not in angleA][0])
    angleB = [hull[(midDotIndB - 1) % len(hull)], hull[midDotIndB],
              hull[(midDotIndB + 1) % len(hull)]]
    sin_b = sinA(*angleB)
    angleRadB = math.asin(sin_b)
    # cos_b = sqrt(1 - sin_b * sin_b)
    return abs(angleRadA + angleRadB - math.pi) < 0.001


# dot1 = Dot(-160, 160)
# dot2 = Dot(60, 160)
# dot3 = Dot(-60, 40)
# dot4 = Dot(-40, 120)
dot3 = Dot(0, 0)
dot1 = Dot(4, 2)
dot2 = Dot(11, 4)
# dot4 = Dot(0.5, -0.3)
dot4 = Dot(8, 2)
print(checkDelone1(dot1, dot2, dot3, dot4))
print(sinA(dot3, dot4, dot1))
print(sinB(dot3, dot4, dot1))

# print(sin(dot1, dot2, dot3))

arr = np.array([1, 2, 3])
a, b, c = list(arr)
