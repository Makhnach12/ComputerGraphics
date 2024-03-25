from Lab2.Parameters import MATRIX_DOWN, MATRIX_UP
from Lab2.dot import Dot

START_POSITION = [(0, 0), (-10, -10), (-30, 0), (-40, 0), (-60, 10),
                  (-60, 30), (-70, 40), (-90, 50), (-90, 10), (-130, -10),
                  (-120, -20), (-110, -20), (-90, -10), (-50, -30), (-50, -40),
                  (-30, -50), (-40, -60), (-100, -90), (-90, -100), (-60, -100),
                  (-20, -80), (0, -80), (20, -70), (50, -70), (70, -80),
                  (120, -80), (130, -70), (130, -50), (120, -40), (100, -30),
                  (150, 20), (140, 30), (130, 30), (60, 0), (0, 0)]
RIGHT_WING = [(-40, 0), (-30, 20), (-40, 30), (-60, 20)]
LEFT_WING = [(-30, -50), (-10, -40), (50, -40), (60, -50), (60, -60),
             (50, -70)]
PLANE_NOSE = [(110, -80), (100, -70), (100, -50), (120, -40)]
DOTES_CABIN_1 = [(-10, -10), (0, -10), (0, 0), (10, -10), (10, 0), (20, -10),
                 (30, -10), (40, -10), (40, -30), (100, -30), (80, -20),
                 (60, -30),
                 (50, -30), (0, -20), (70, -20), (60, -10), (60, 0)]
DOTES_CABIN_2 = [(20, -10), (30, 0), (40, 0), (30, -10), (40, -10), (50, -10),
                 (50, 0)]
DOTES_CABIN_3 = [(50, -30), (50, -10), (30, -20), (30, -10)]


class Plane:
    def __init__(self, canvas):
        self.__canvas = canvas
        self.lines1: list = []
        self.lines2: list = []
        self.lines3: list = []
        self.lines4: list = []
        self.lines5: list = []
        self.lines6: list = []
        self.lines7: list = []
        self.dotes1: list[Dot] = [Dot(*coords) for coords in START_POSITION]
        self.dotes2: list[Dot] = [Dot(*coords) for coords in RIGHT_WING]
        self.dotes3: list[Dot] = [Dot(*coords) for coords in LEFT_WING]
        self.dotes4: list[Dot] = [Dot(*coords) for coords in PLANE_NOSE]
        self.dotes5: list[Dot] = [Dot(*coords) for coords in DOTES_CABIN_1]
        self.dotes6: list[Dot] = [Dot(*coords) for coords in DOTES_CABIN_2]
        self.dotes7: list[Dot] = [Dot(*coords) for coords in DOTES_CABIN_3]
        self.dotes = [self.dotes1, self.dotes2, self.dotes3, self.dotes4,
                      self.dotes5, self.dotes6, self.dotes7]
        for i in range(0, len(self.dotes1) - 1):
            self.lines1.append(
                canvas.create_line(self.dotes1[i].coors,
                                   self.dotes1[i + 1].coors,
                                   fill='red', width=2))
        for i in range(0, len(self.dotes2) - 1):
            self.lines2.append(
                canvas.create_line(self.dotes2[i].coors,
                                   self.dotes2[i + 1].coors,
                                   fill='red', width=2))
        for i in range(0, len(self.dotes3) - 1):
            self.lines3.append(
                canvas.create_line(self.dotes3[i].coors,
                                   self.dotes3[i + 1].coors,
                                   fill='red', width=2))

        for i in range(0, len(self.dotes4) - 1):
            self.lines4.append(
                canvas.create_line(self.dotes4[i].coors,
                                   self.dotes4[i + 1].coors,
                                   fill='red', width=2))
        self.lines7.append(canvas.create_line(self.dotes7[0].coors,
                                              self.dotes7[1].coors,
                                              fill='red', width=2))
        self.lines7.append(canvas.create_line(self.dotes7[-1].coors,
                                              self.dotes7[-2].coors,
                                              fill='red', width=2))

        self.lines6.append(canvas.create_line(self.dotes5[-1].coors,
                                              self.dotes6[-2].coors,
                                              fill='red', width=2))
        self.lines6.append(canvas.create_line(self.dotes6[-1].coors,
                                              self.dotes6[-3].coors,
                                              fill='red', width=2))
        self.lines6.append(canvas.create_line(self.dotes6[2].coors,
                                              self.dotes6[3].coors,
                                              fill='red', width=2))
        self.lines6.append(canvas.create_line(self.dotes6[1].coors,
                                              self.dotes6[0].coors,
                                              fill='red', width=2))

        self.lines5.append(canvas.create_line(self.dotes5[0].coors,
                                              self.dotes5[3].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[3].coors,
                                              self.dotes5[4].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[3].coors,
                                              self.dotes5[-2].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-1].coors,
                                              self.dotes5[-2].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[3].coors,
                                              self.dotes5[-5].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-5].coors,
                                              self.dotes5[-6].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-6].coors,
                                              self.dotes5[-7].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-1].coors,
                                              self.dotes5[-7].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-8].coors,
                                              self.dotes5[-7].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-1].coors,
                                              self.dotes5[-6].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-3].coors,
                                              self.dotes5[-6].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-3].coors,
                                              self.dotes5[-7].coors,
                                              fill='red', width=2))
        self.lines5.append(canvas.create_line(self.dotes5[-3].coors,
                                              self.dotes5[-1].coors,
                                              fill='red', width=2))

    def __changeCoors(self, mat):
        for dot in self.dotes1:
            dot.multMat(mat)
        for dot in self.dotes2:
            dot.multMat(mat)
        for dot in self.dotes3:
            dot.multMat(mat)
        for dot in self.dotes4:
            dot.multMat(mat)
        for dot in self.dotes5:
            dot.multMat(mat)
        for dot in self.dotes6:
            dot.multMat(mat)
        for dot in self.dotes7:
            dot.multMat(mat)
        self.__changeLines()

    def __changeLines(self):
        for i in range(0, len(self.dotes1) - 1):
            self.__canvas.coords(self.lines1[i], *self.dotes1[i].coors,
                                 *self.dotes1[i + 1].coors)
        for i in range(0, len(self.dotes2) - 1):
            self.__canvas.coords(self.lines2[i], *self.dotes2[i].coors,
                                 *self.dotes2[i + 1].coors)
        for i in range(0, len(self.dotes3) - 1):
            self.__canvas.coords(self.lines3[i], *self.dotes3[i].coors,
                                 *self.dotes3[i + 1].coors)
        for i in range(0, len(self.dotes4) - 1):
            self.__canvas.coords(self.lines4[i], *self.dotes4[i].coors,
                                 *self.dotes4[i + 1].coors)

        self.__canvas.coords(self.lines7[0], *self.dotes7[0].coors,
                             *self.dotes7[1].coors)
        self.__canvas.coords(self.lines7[1], *self.dotes7[-1].coors,
                             *self.dotes7[-2].coors)
        self.__canvas.coords(self.lines6[0], *self.dotes5[-1].coors,
                             *self.dotes6[-2].coors)
        self.__canvas.coords(self.lines6[1], *self.dotes6[-1].coors,
                             *self.dotes6[-3].coors)
        self.__canvas.coords(self.lines6[2], *self.dotes6[3].coors,
                             *self.dotes6[3].coors)
        self.__canvas.coords(self.lines6[3], *self.dotes6[1].coors,
                             *self.dotes6[0].coors)
        self.__canvas.coords(self.lines5[0], *self.dotes5[0].coors,
                             *self.dotes5[3].coors)
        self.__canvas.coords(self.lines5[1], *self.dotes5[3].coors,
                             *self.dotes5[4].coors)
        self.__canvas.coords(self.lines5[2], *self.dotes5[3].coors,
                             *self.dotes5[-2].coors)
        self.__canvas.coords(self.lines5[3], *self.dotes5[-1].coors,
                             *self.dotes5[-2].coors)
        self.__canvas.coords(self.lines5[4], *self.dotes5[3].coors,
                             *self.dotes5[-5].coors)
        self.__canvas.coords(self.lines5[5], *self.dotes5[-5].coors,
                             *self.dotes5[-6].coors)
        self.__canvas.coords(self.lines5[6], *self.dotes5[-6].coors,
                             *self.dotes5[-7].coors)
        self.__canvas.coords(self.lines5[7], *self.dotes5[-1].coors,
                             *self.dotes5[-7].coors)
        self.__canvas.coords(self.lines5[8], *self.dotes5[-8].coors,
                             *self.dotes5[-7].coors)
        self.__canvas.coords(self.lines5[9], *self.dotes5[-1].coors,
                             *self.dotes5[-6].coors)
        self.__canvas.coords(self.lines5[10], *self.dotes5[-3].coors,
                             *self.dotes5[-6].coors)
        self.__canvas.coords(self.lines5[11], *self.dotes5[-3].coors,
                             *self.dotes5[-7].coors)
        self.__canvas.coords(self.lines5[12], *self.dotes5[-3].coors,
                             * self.dotes5[-1].coors)

    def shiftDown(self):
        self.__changeCoors(MATRIX_DOWN)

    def shiftUp(self):
        self.__changeCoors(MATRIX_UP)
