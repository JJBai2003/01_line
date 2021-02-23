from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    x = int(x0)
    y = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    dx = x1 - x0
    dy = y1 - y0

    if (x1 < x): 
        x = x1
        y = y1
        x1 = x0
        y1 = y0
        dx = -dx
        dy = -dy

    if (dy==0): 
        for x in range(x,x1+1):
            plot(screen, color,x,y)
            x += 1
    elif (dx == 0):
        for y in range(y, y1+1):
            plot(screen, color, x, y)
            y+= 1

    elif (dy <= dx and dy > 0):
        A = dy
        B = -dx
        d = 2 * A + B
        while x <= x1:
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2*A 
    elif (dy > dx):
        A = dx
        B = -dy
        d = 2 * A + B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * B
            y += 1
            d += 2 * A
    elif (-dy > dx):
        A = dx
        B = -dy
        d = 2 * A - B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d -= 2 * B
            y -= 1
            d += 2 * A
    else:
        A = dy
        B = -dx
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x+=1
            d += 2 * A
    







