import numpy as np

from Lab2.Parameters import getMatrixTurning, getMatrixTurningToPoint, \
    MATRIX_DOWN, MATRIX_UP
from Lab2.dot import Dot

FIRST_VINT = [(120, -60), (110, -50), (110, -30), (120, -20),
              (130, -30), (130, -50), (120, -60), (110, -70), (110, -90),
              (120, -100), (130, -90), (130, -70), (120, -60)]


class Propeller:
    def __init__(self, canvas, root):
        self.mid = [120, -60]
        self.__root = root
        self.__canvas = canvas
        self.__lines = []
        self.__dotes: list[Dot] = [Dot(*coords) for coords in
                                   FIRST_VINT]
        for i in range(0, len(self.__dotes) - 1):
            self.__lines.append(self.__canvas.create_line(self.__dotes[i].coors,
                                                          self.__dotes[
                                                              i + 1].coors,
                                                          fill='green',
                                                          width=2))

    def __changeLines(self):
        for i in range(0, len(self.__dotes) - 1):
            self.__canvas.coords(self.__lines[i], *self.__dotes[i].coors,
                                 *self.__dotes[i + 1].coors)

    def __changeCoors(self, mat):
        for dot in self.__dotes:
            dot.multMat(mat)
        self.__changeLines()

    def turnPropeller(self, angle: int = 5):
        angle = (angle * np.pi) / 180
        self.__changeCoors(getMatrixTurningToPoint(self.mid, 10))
        self.__root.after(100, self.turnPropeller)

    def shiftDown(self):
        self.mid[1] -= 1
        self.__changeCoors(MATRIX_DOWN)

    def shiftUp(self):
        self.mid[1] += 1
        self.__changeCoors(MATRIX_UP)
