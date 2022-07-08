def my_triange_square(x, y):
    if x <= 0 or y <= 0:
        raise Exception("Площадь треугольника меньше 0")
    else:
        s = 0.5 * x * y
        return s

def my_triange_perimetr(x, y, z):
    if x <= 0 or y <= 0 or z <=0:
        raise Exception("Периметр треугольника меньше 0")
    else:
        p = x + y + z
        return p
