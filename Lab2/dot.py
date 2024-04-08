from math import sqrt

import numpy as np

from Lab2.Parameters import MIDDLE


class Dot:
    def __init__(self, x, y, z=1):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def multMat(self, mat):
        newCoors = list(np.dot([self.__x, self.__y, self.__z], mat))
        self.__x, self.__y, self.__z = newCoors[0], newCoors[1], newCoors[2]

    @property
    def coors(self):
        return MIDDLE[0] + self.__x, MIDDLE[1] - self.__y

    @property
    def coorsNorm(self):
        return self.__x, self.__y

    def __add__(self, dot):
        return Dot(self.__x + dot.x, self.__y + dot.y)

    def __truediv__(self, num: int):
        return Dot(self.__x / num, self.__y / num)

    def dist(self, dot):
        return sqrt((dot.x - self.__x) ** 2 + (dot.y - self.__y) ** 2)

    def __str__(self):
        return f'{self.__x} {self.__y}'



