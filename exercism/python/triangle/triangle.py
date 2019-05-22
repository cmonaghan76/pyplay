def is_equilateral(sides):
    if is_triangle(sides):
        if len(reduce_list(sides)) == 1:
            return True
        else:
            return False
    else:
        return False


def is_isosceles(sides):
    if is_triangle(sides):
        if len(reduce_list(sides)) < 3:
            return True
        else:
            return False
    else:
        return False


def is_scalene(sides):
    if is_triangle(sides):
        if len(reduce_list(sides)) == 3:
            return True
        else:
            return False
    else:
        return False 


def reduce_list(sides):
    return list(dict.fromkeys(sides))


def is_triangle(sides):
    if len(sides) == 3 and \
        all(i != 0 for i in sides) and \
        sides[0] + sides[1] > sides[2] and \
        sides[1] + sides[2] > sides[0] and \
        sides[2] + sides[0] > sides[1]:
        return True
    else:
        return False