def my_reactangle_square(a, b):
    if a <= 0 or b <= 0:
        raise Exception("Площадь прямоугольника меньше 0")
    else:
        s = a * b
        return s

def my_reactangle_perimetr(a, b):
    if a <= 0 or b <= 0:
        raise Exception("Периметр прямоугольника меньше 0")
    else:
        p = 2*(a + b)
        return p
