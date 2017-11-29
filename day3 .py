import math


class QuaError(Exception): pass


def quad(a, b, c):
    if a == 0:
        ex = QuaError("Not Quadratic")
        ex.cf = (a, b, c)
        raise ex
    if b * b - 4 * a * c < 0:
        mm = QuaError("No Real Roots")
        mm.cf = (a, b, c)
        raise mm
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return (x1, x2)


def qu(a, b, c):
    try:
        x1, x2 = quad(a, b, c)
        print("Roots are", x1, x2)
    except QuaError as e:
        print(e, e.cf)


qu(2, 3, 4)
