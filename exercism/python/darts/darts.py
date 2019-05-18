# Solution by Christopher Monaghan
# May 18, 2019

def score(x, y):
    import math
    dart_distance = math.sqrt(x**2 + y**2)
    if dart_distance >= 0 and dart_distance <= 1:
        return 10
    elif dart_distance > 1 and dart_distance <= 5:
        return 5
    elif dart_distance > 5 and dart_distance <= 10:
        return 1
    else:
        return 0