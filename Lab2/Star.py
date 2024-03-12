import numpy as np

from Lab2.Parameters import HEIGHT, WIDTH, MATRIX_DOWN, MATRIX_UP, MATRIX_LEFT, \
    MATRIX_RIGHT, MATRIX_OX, MATRIX_OY, MATRIX_XY, SCALE_X_UP, \
    SCALE_Y_UP, SCALE_X_DOWN, SCALE_Y_DOWN, getMatrixTurning
from Lab2.dot import Dot


class Star:
    def __init__(self, canvas):
        self.__canvas = canvas
        self.__lines: list = []
        self.__dotes: list[Dot] = []
        self.__dotes.append(Dot(-50, -68))
        self.__dotes.append(Dot(0, -32))
        self.__dotes.append(Dot(50, -68))
        self.__dotes.append(Dot(30, -10))
        self.__dotes.append(Dot(80, 26))
        self.__dotes.append(Dot(18, 26))
        self.__dotes.append(Dot(0, 80))
        self.__dotes.append(Dot(-18, 26))
        self.__dotes.append(Dot(-80, 26))
        self.__dotes.append(Dot(-30, -10))
        self.__dotes.append(Dot(- 50, -68))

        for i in range(0, len(self.__dotes) - 1):
            self.__lines.append(self.__canvas.create_line(self.__dotes[i].coors,
                                                          self.__dotes[
                                                              i + 1].coors,
                                                          fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[0].coors,
                                      self.__dotes[-1].coors,
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[-2].coors,
                                      self.__dotes[1].coors,
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[3].coors,
                                      self.__dotes[1].coors,
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[-5].coors,
                                      self.__dotes[1].coors,
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[-4].coors,
                                      self.__dotes[1].coors,
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__dotes[-6].coors,
                                      self.__dotes[1].coors,
                                      fill='red', width=2))

    def __changeLines(self):
        for i in range(0, len(self.__dotes) - 1):
            self.__canvas.coords(self.__lines[i], *self.__dotes[i].coors,
                                 *self.__dotes[i + 1].coors)
        self.__canvas.coords(self.__lines[len(self.__dotes)],
                             *self.__dotes[-2].coors,
                             *self.__dotes[1].coors)
        self.__canvas.coords(self.__lines[len(self.__dotes) + 1],
                             *self.__dotes[3].coors,
                             *self.__dotes[1].coors)
        self.__canvas.coords(self.__lines[len(self.__dotes) + 2],
                             *self.__dotes[-5].coors,
                             *self.__dotes[1].coors)
        self.__canvas.coords(self.__lines[len(self.__dotes) + 3],
                             *self.__dotes[-4].coors,
                             *self.__dotes[1].coors)
        self.__canvas.coords(self.__lines[len(self.__dotes) + 4],
                             *self.__dotes[-6].coors,
                             *self.__dotes[1].coors)

    def __changeCoors(self, mat):
        for dot in self.__dotes:
            dot.multMat(mat)
        self.__changeLines()

    def shiftDown(self):
        self.__changeCoors(MATRIX_DOWN)

    def shiftUp(self):
        self.__changeCoors(MATRIX_UP)

    def shiftLeft(self):
        self.__changeCoors(MATRIX_LEFT)

    def shiftRight(self):
        self.__changeCoors(MATRIX_RIGHT)

    def reflectOX(self):
        self.__changeCoors(MATRIX_OX)

    def reflectOY(self):
        self.__changeCoors(MATRIX_OY)

    def reflect(self):
        self.__changeCoors(MATRIX_XY)

    def scaleOX_UP(self):
        self.__changeCoors(SCALE_X_UP)

    def scaleOY_UP(self):
        self.__changeCoors(SCALE_Y_UP)

    def scaleOX_DOWN(self):
        self.__changeCoors(SCALE_X_DOWN)

    def scaleOY_DOWN(self):
        self.__changeCoors(SCALE_Y_DOWN)

    def turnStar(self, angle: int):
        angle = (angle * np.pi) / 180
        self.__changeCoors(getMatrixTurning(angle))


