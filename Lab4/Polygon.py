from Lab2.dot import Dot
from Lab3.Line import RAD


class Polygon:
    def __init__(self, canvas):
        self.canvasDots = []
        self.__dots = []
        self.canvasLines = []
        self.__canvas = canvas

    def addDot(self, dot: Dot):
        if dot not in self.__dots:
            self.__dots.append(dot)
            self.canvasDots.append(self.__canvas.create_oval(dot.coors[0] - RAD,
                                                             dot.coors[1] - RAD,
                                                             dot.coors[0] + RAD,
                                                             dot.coors[1] + RAD))
            if len(self.__dots) > 1:
                self.canvasLines.append(self.__canvas.create_line(
                    self.__dots[len(self.__dots) - 2].coors,
                    self.__dots[len(self.__dots) - 1].coors,
                    fill='green', width=2))
        else:
            self.canvasLines.append(self.__canvas.create_line(
                self.__dots[0].coors,
                self.__dots[len(self.__dots) - 1].coors,
                fill='green', width=2))

    @property
    def coors(self):
        return [self.__dots[0].coorsNorm[0],
                self.__dots[0].coorsNorm[1],
                self.__dots[2].coorsNorm[0],
                self.__dots[2].coorsNorm[1]]

    def clearPolygon(self):
        for elem in self.canvasDots:
            self.__canvas.delete(elem)
        self.__dots.clear()
        for elem in self.canvasLines:
            self.__canvas.delete(elem)
        self.canvasLines.clear()


class Rectangle(Polygon):
    def __init__(self, canvas, dotLeft, dotRight):
        super().__init__(canvas)
        self.addDot(dotLeft)
        dotLeftBottom = Dot(dotLeft.coorsNorm[0], dotRight.coorsNorm[1])
        self.addDot(dotLeftBottom)
        self.addDot(dotRight)
        dotRightTop = Dot(dotRight.coorsNorm[0], dotLeft.coorsNorm[1])
        self.addDot(dotRightTop)
        self.addDot(dotLeft)
