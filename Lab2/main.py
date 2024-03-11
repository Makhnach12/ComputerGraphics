# import tkinter
# import math
#
# from Lab2.Star import Star
#
# master = tkinter.Tk()
# canvas = tkinter.Canvas(master, bg='white', height=601, width=601)
# canvas.pack()
# st = Star((300, 300))
# st.printStar(canvas)
# #
# # p1 = (300, 332)
# # p2 = (250, 368)
# # canvas.create_line(p1, p2, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (350, 368)
# # canvas.create_line(p1, p3, fill = 'red')
# #
# # p1 = (330, 310)
# # p3 = (350, 368)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (330, 310)
# # p3 = (380, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (318, 274)
# # p3 = (380, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (318, 274)
# # p3 = (300, 220)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (282, 274)
# # p3 = (300, 220)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (282, 274)
# # p3 = (220, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (270, 310)
# # p3 = (220, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (270, 310)
# # p3 = (250, 368)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (300, 220)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (270, 310)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (330, 310)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (318, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# #
# # p1 = (300, 332)
# # p3 = (282, 274)
# # canvas.create_line(p3, p1, fill = 'red')
# master.mainloop()
# import tkinter as tk
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()
#
# # Рисуем вертикальные линии
# for i in range(0, 400, 20):
#     canvas.create_line(i, 0, i, 400, fill="gray")
#
# # Рисуем горизонтальные линии
# for i in range(0, 400, 20):
#     canvas.create_line(0, i, 400, i, fill="gray")

# root.mainloop()
from Lab2.Root import Window

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()
win = Window()
# win.createStar(300, 300)
# win.shiftStar(100, 100)
win.root.mainloop()