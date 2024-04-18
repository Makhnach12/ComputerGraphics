from Lab2.Root import CELL_SIZE
from Lab2.dot import Dot
from Lab3.Line import RAD


def draw_line(start: Dot, end: Dot):
    line_pixel = []
    (x1, y1) = start.coorsNorm
    (x2, y2) = end.coorsNorm
    dx = x2 - x1
    dy = y2 - y1

    sign_x = CELL_SIZE if dx > 0 else -CELL_SIZE if dx < 0 else 0
    sign_y = CELL_SIZE if dy > 0 else -CELL_SIZE if dy < 0 else 0

    if dx < 0: dx = -dx
    if dy < 0: dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += CELL_SIZE
        line_pixel.append(Dot(x, y))
    return line_pixel[:len(line_pixel) - 1:]


def printBorder(method):
    def wrapper(*args, **kwargs):
        verts = args[0].vertices
        dots = []
        if 'printBord' in kwargs and kwargs['printBord']:
            if len(verts) > 0:
                dots = draw_line(verts[-1], args[1])
            for elem in dots:
                args[0].canvasDots.append(args[0].canvas.create_oval(
                    elem.coors[0] - RAD,
                    elem.coors[1] - RAD,
                    elem.coors[0] + RAD,
                    elem.coors[1] + RAD)
                )
                args[0].borderDots.append(elem)
        return method(*args, **kwargs)

    return wrapper


def checkerDotInList(arr: list, dot: Dot):
    for elem in arr:
        if elem == dot:
            return True
    return False


class Polygon:
    def __init__(self, canvas):
        self.canvasDots = []
        self.__dots = []
        self.canvasLines = []
        self.borderDots = []
        self.__canvas = canvas

    @printBorder
    def addDot(self, dot: Dot, printBord=False):
        if not checkerDotInList(self.__dots, dot):
            self.__dots.append(dot)
            self.canvasDots.append(self.__canvas.create_oval(dot.coors[0] - RAD,
                                                             dot.coors[1] - RAD,
                                                             dot.coors[0] + RAD,
                                                             dot.coors[1] + RAD)
                                   )
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

    @property
    def canvas(self):
        return self.__canvas

    def clearPolygon(self):
        for elem in self.canvasDots:
            self.__canvas.delete(elem)
        self.__dots.clear()
        for elem in self.canvasLines:
            self.__canvas.delete(elem)
        self.canvasLines.clear()
        self.borderDots.clear()

    @property
    def vertices(self):
        return self.__dots.copy()


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
