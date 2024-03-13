import tkinter as tk
import time

from Lab2.Propeller import Propeller
from Lab2.Root import Window, drawGrid
from Lab2.dot import Dot


#
# win = Window()
# win.root.mainloop()

def drawCabin(lines):
    dotes = [(-10, -10), (0, -10), (0, 0), (10, -10), (10, 0), (20, -10),
             (30, -10), (40, -10), (40, -30), (100, -30), (80, -20), (60, -30),
             (50, -30), (0, -20), (70, -20), (60, -10), (60, 0)]
    dotes12 = [(20, -10), (30, 0), (40, 0), (30, -10), (40, -10), (50, -10),
               (50, 0)]
    dotes13 = [(50, -30), (50, -10), (30, -20), (30, -10)]
    dotes1: list[Dot] = [Dot(*coords) for coords in dotes]
    dotes2: list[Dot] = [Dot(*coords) for coords in dotes12]
    dotes3: list[Dot] = [Dot(*coords) for coords in dotes13]

    lines.append(canvas.create_line(dotes3[0].coors, dotes3[1].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes3[-1].coors, dotes3[-2].coors,
                                    fill='red', width=2))

    lines.append(canvas.create_line(dotes1[-1].coors, dotes2[-2].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes2[-1].coors, dotes2[-3].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes2[2].coors, dotes2[3].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes2[1].coors, dotes2[0].coors,
                                    fill='red', width=2))

    lines.append(canvas.create_line(dotes1[0].coors, dotes1[3].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[3].coors, dotes1[4].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[3].coors, dotes1[-2].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-1].coors, dotes1[-2].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[3].coors, dotes1[-5].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-5].coors, dotes1[-6].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-6].coors, dotes1[-7].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-1].coors, dotes1[-7].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-8].coors, dotes1[-7].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-1].coors, dotes1[-6].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-3].coors, dotes1[-6].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-3].coors, dotes1[-7].coors,
                                    fill='red', width=2))
    lines.append(canvas.create_line(dotes1[-3].coors, dotes1[-1].coors,
                                    fill='red', width=2))


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
root = tk.Tk()
root.title("LAB2.COM")
canvas = tk.Canvas(root, width=600, height=600, background='#F7F6E7')
canvas.pack()
drawGrid(canvas, '#C1C0B9')
lines: list = []
dotes1: list[Dot] = [Dot(*coords) for coords in START_POSITION]
dotes2: list[Dot] = [Dot(*coords) for coords in RIGHT_WING]
dotes3: list[Dot] = [Dot(*coords) for coords in LEFT_WING]
dotes4: list[Dot] = [Dot(*coords) for coords in PLANE_NOSE]
for i in range(0, len(dotes1) - 1):
    lines.append(canvas.create_line(dotes1[i].coors, dotes1[i + 1].coors,
                                    fill='red', width=2))
for i in range(0, len(dotes2) - 1):
    lines.append(canvas.create_line(dotes2[i].coors, dotes2[i + 1].coors,
                                    fill='red', width=2))
for i in range(0, len(dotes3) - 1):
    lines.append(canvas.create_line(dotes3[i].coors, dotes3[i + 1].coors,
                                    fill='red', width=2))

for i in range(0, len(dotes4) - 1):
    lines.append(canvas.create_line(dotes4[i].coors, dotes4[i + 1].coors,
                                    fill='red', width=2))
drawCabin(lines)
p = Propeller(canvas, root)

p.turnPropeller()
root.mainloop()
