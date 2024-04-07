from Lab2.dot import Dot

INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


def computeCode(dot: Dot, ):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP
    return code


def hitung():
    x1 = float(entry_x1.get())
    y1 = float(entry_y1.get())
    x2 = float(entry_x2.get())
    y2 = float(entry_y2.get())

    my_canvas.create_line(x1, y1, x2, y2, fill='red')
    my_canvas.grid(row=6, column=0)

    # region = [x1, y1, x2, y2]

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:

            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

                # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1)
                x = x_min

                # Now intersection point x, y is found
            # We replace point outside clipping rectangle
            # by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        my_canvas.create_line(x1, y1, x2, y2, fill='blue', width=1)
        my_canvas.grid(row=6, column=0)
        # Here the user can add code to display the rectangle
        # along with the accepted (portion of) lines

    else:
        print("Line rejected")
