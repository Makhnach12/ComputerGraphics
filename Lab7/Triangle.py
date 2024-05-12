from dataclasses import dataclass

from Lab2.dot import Dot


@dataclass
class Rib:
    dotSt: Dot
    dotFn: Dot

    @property
    def dots(self):
        return [self.dotSt, self.dotFn]

    def __repr__(self):
        return f'{self.dotSt} {self.dotFn}'

    def __hash__(self):
        return hash(Rib.__repr__(self))


class Triangle:
    def __init__(self, A, B, C):
        self.Nodes = [A, B, C]
        self.ribs = [Rib(A, B), Rib(B, C), Rib(C, A)]
        self.neighborTriangles = {}
        self.canvasLines = []

    def addNeighbor(self, *triangles):
        for triangle in triangles:
            sameDots: list[Dot] = [dot for dot in self.Nodes
                                   if dot in triangle.Nodes]
            if len(sameDots) < 2:
                continue
            rib = [rib for rib in self.ribs if set(rib.dots) == set(sameDots)]
            self.neighborTriangles[*rib] = triangle

    def __str__(self):
        return f'{self.Nodes}'

    def drawTriangle(self, canvas):
        self.canvasLines.extend(
            [canvas.create_line(self.Nodes[0].coors, self.Nodes[1].coors,
                                fill='white', width=2),
             canvas.create_line(self.Nodes[1].coors, self.Nodes[2].coors,
                                fill='white', width=2),
             canvas.create_line(self.Nodes[2].coors, self.Nodes[0].coors,
                                fill='white', width=2)])
