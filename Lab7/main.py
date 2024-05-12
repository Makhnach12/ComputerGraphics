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
import numpy as np

from Lab2.dot import Dot
from Lab6.Window import bruteHull


# from Lab1.launchPY.mainFunctions import getAngle
# from Lab2.dot import Dot
# from Lab7.Window import checkAngle, checkDelone

# arr = {gg: 'gg', gg2: 'gg2'}
# print(arr[Rib(Dot(0, 1), Dot(1, 1))])

# from Lab7.Window import WindowTriangulation
#
# win = WindowTriangulation()
# win.root.mainloop()
# a,b = (0,0 )
# print(a, b)
# dot1 = Dot(20, 160)
# dot2 = Dot(-80, 60)
# dot3 = Dot(-160, 160)
# dot4 = Dot(-60, 140)
# print(getAngle(dot1, dot2, dot3))
# print(checkAngle(dot1, dot2, dot3))
# print(checkDelone(dot1, dot2, dot3, dot4))

def sort_coordinates(list_of_xy_coords):
    cx, cy = list_of_xy_coords.mean(0)
    x, y = list_of_xy_coords.T
    angles = np.arctan2(x - cx, y - cy)
    indices = np.argsort(angles)
    return indices


def checkDelone(p1: Dot, p2: Dot, p3: Dot, p0: Dot) -> bool:
    s_a = (p0.x - p1.x) * (p0.x - p3.x) + (p0.y - p1.y) * (p0.y - p3.y)
    s_b = (p2.x - p1.x) * (p2.x - p3.x) + (p2.y - p1.y) * (p2.y - p3.y)
    if s_a < 0 and s_b < 0:
        return False
    elif s_a >= 0 and s_b >= 0:
        return True
    if len(bruteHull([p0, p1, p2, p3])) == 3:
        return False
    cos_a = (p0.x - p1.x) * (p0.x - p3.x) + (p0.y - p1.y) * (p0.y - p3.y)
    cos_b = (p2.x - p1.x) * (p2.x - p3.x) + (p2.y - p1.y) * (p2.y - p3.y)
    sin_a = (p0.x - p1.x) * (p0.y - p3.y) - (p0.x - p3.x) * (p0.y - p1.y)
    sin_b = (p2.x - p1.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p2.y - p1.y)
    return sin_a * cos_b + cos_a * sin_b >= 0


# dot1 = Dot(-160, 160)
# dot2 = Dot(60, 160)
# dot3 = Dot(-60, 40)
# dot4 = Dot(-40, 120)
dot1 = Dot(2, 0)
dot2 = Dot(2, -2)
dot3 = Dot(0, -2)
dot4 = Dot(0, 0)
print(checkDelone(dot1, dot2, dot3, dot4))

arr = np.array([1, 2, 3])
a, b, c = list(arr)
