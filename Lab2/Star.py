from Lab2.Parameters import HEIGHT, WIDTH


class Star:
    def __init__(self, canvas, center: (int, int) = (0, 0)):
        self.__canvas = canvas
        self.__lines: list = []
        self.__coors: list = []
        self.__coors.append([center[0] - 50, center[1] + 68])
        self.__coors.append([center[0], center[1] + 32])
        self.__coors.append([center[0] + 50, center[1] + 68])
        self.__coors.append([center[0] + 30, center[1] + 10])
        self.__coors.append([center[0] + 80, center[1] - 26])
        self.__coors.append([center[0] + 18, center[1] - 26])
        self.__coors.append([center[0], center[1] - 80])
        self.__coors.append([center[0] - 18, center[1] - 26])
        self.__coors.append([center[0] - 80, center[1] - 26])
        self.__coors.append([center[0] - 30, center[1] + 10])
        self.__coors.append([center[0] - 50, center[1] + 68])

        for i in range(0, len(self.__coors) - 1):
            self.__lines.append(self.__canvas.create_line(self.__coors[i],
                                                          self.__coors[i + 1],
                                                          fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[0], self.__coors[-1],
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[-2], self.__coors[1],
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[3], self.__coors[1],
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[-5], self.__coors[1],
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[-4], self.__coors[1],
                                      fill='red', width=2))
        self.__lines.append(
            self.__canvas.create_line(self.__coors[-6], self.__coors[1],
                                      fill='red', width=2))

    def __changeLines(self, newCoorsList: list[(int, int)]):
        for i in range(0, len(newCoorsList) - 1):
            self.__canvas.coords(self.__lines[i], *(newCoorsList[i] +
                                                    newCoorsList[i + 1]))
        self.__canvas.coords(self.__lines[len(newCoorsList) - 1],
                             *(newCoorsList[0] + newCoorsList[-1]))
        self.__canvas.coords(self.__lines[len(newCoorsList)],
                             *(newCoorsList[-2] + newCoorsList[1]))
        self.__canvas.coords(self.__lines[len(newCoorsList) + 1],
                             *(newCoorsList[3] + newCoorsList[1]))
        self.__canvas.coords(self.__lines[len(newCoorsList) + 2],
                             *(newCoorsList[-5] + newCoorsList[1]))
        self.__canvas.coords(self.__lines[len(newCoorsList) + 3],
                             *(newCoorsList[-4] + newCoorsList[1]))
        self.__canvas.coords(self.__lines[len(newCoorsList) + 4],
                             *(newCoorsList[-6] + newCoorsList[1]))

    def __changeCoors(self, shift_x: int, shift_y: int):
        for coors in self.__coors:
            coors[0] += shift_x
            coors[1] += shift_y
        self.__changeLines(self.__coors)

    def shiftDown(self):
        self.__changeCoors(0, 5)

    def shiftUp(self):
        self.__changeCoors(0, -5)

    def shiftLeft(self):
        self.__changeCoors(-5, 0)

    def shiftRight(self):
        self.__changeCoors(5, 0)

    def reflectOX(self):
        for coors in self.__coors:
            if coors[1] > HEIGHT // 2:
                coors[1] = HEIGHT // 2 - (coors[1] - HEIGHT // 2)
            elif coors[1] < HEIGHT // 2:
                coors[1] = HEIGHT // 2 + (HEIGHT // 2 - coors[1])
        self.__changeLines(self.__coors)

    def reflectOY(self):
        for coors in self.__coors:
            if coors[0] > WIDTH // 2:
                coors[0] = WIDTH // 2 - (coors[0] - WIDTH // 2)
            elif coors[0] < WIDTH // 2:
                coors[0] = WIDTH // 2 + (WIDTH // 2 - coors[0])
        self.__changeLines(self.__coors)
