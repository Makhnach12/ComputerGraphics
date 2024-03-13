import tkinter as tk
import time

from Lab2.Plane import Plane
from Lab2.Propeller import Propeller
from Lab2.Root import Window, drawGrid
from Lab2.dot import Dot

win = Window()
win.root.mainloop()


# root = tk.Tk()
# root.title("LAB2.COM")
# canvas = tk.Canvas(root, width=600, height=600, background='#F7F6E7')
# canvas.pack()
# drawGrid(canvas, '#C1C0B9')
# plane = Plane(canvas)
# p = Propeller(canvas, root)
#
# SUM = 0
#
#
# def goDown():
#     global SUM
#     p.shiftDown()
#     plane.shiftDown()
#     SUM += 100
#     if SUM // 1000 % 2 == 0:
#         root.after(100, goDown)
#     else:
#         root.after(100, goUp)
#
#
# def goUp():
#     global SUM
#     p.shiftUp()
#     plane.shiftUp()
#     SUM += 100
#     if SUM // 1000 % 2 == 0:
#         root.after(100, goDown)
#     else:
#         root.after(100, goUp)
#
#
# goDown()
# p.turnPropeller()
# root.mainloop()
