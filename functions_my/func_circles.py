import math

def my_circle_square(radius):
    if radius <= 0:
        raise Exception("Площадь круга меньше 0")
    else:
        return math.pi * (radius ** 2)

def my_circle_perimetr(radius):
    if radius <= 0:
        raise Exception("Периметр круга меньше 0")
    else:
        p = 2 * math.pi * radius
        return p
