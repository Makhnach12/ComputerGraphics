from Lab2.dot import Dot
from Lab3.Line import RAD


class Circle:
    def __init__(self, canvas):
        self.center = Dot(0, 0)
        self.radius = 0
        self.canvas = canvas
        self.canvasOval = None
        self.__rastDots = []
        self.canvasDots = []

    def __changeLines(self):
        self.canvas.coords(self.canvasOval,
                           self.center.coors[0] - self.radius,
                           self.center.coors[1] - self.radius,
                           self.center.coors[0] + self.radius,
                           self.center.coors[1] + self.radius)

    def createCircle(self, center: Dot, radius):
        self.center = center
        self.radius = radius
        if self.canvasOval is None:
            self.canvasOval = self.canvas.create_oval(
                self.center.coors[0] - self.radius,
                self.center.coors[1] - self.radius,
                self.center.coors[0] + self.radius,
                self.center.coors[1] + self.radius)
        else:
            self.__changeLines()

    def printDots(self):
        for dot in self.__rastDots:
            self.canvasDots.append(self.canvas.create_oval(dot.coors[0] - RAD,
                                                           dot.coors[1] - RAD,
                                                           dot.coors[0] + RAD,
                                                           dot.coors[
                                                               1] + RAD))

    def bresenhamAlgorithm(self):
        x, y = self.radius // 20, 0
        delta = 2 * (1 - self.radius // 20)
        while x >= 0:
            self.__rastDots.append(Dot(x * 20, y * 20))
            deltaX = 2 * delta + 2 * x - 1
            deltaY = 2 * delta - 2 * y - 1
            if delta < 0 and deltaX <= 0:
                y += 1
                delta += 2 * y + 1
            elif delta > 0 and deltaY >= 0:
                x -= 1
                delta -= 2 * x - 1
            else:
                x -= 1
                y += 1
                delta += 2 * y - 2 * x + 2
