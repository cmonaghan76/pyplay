def is_armstrong_number(number):
    sum = 0
    digits = list(str(number))
    for n in digits:
        sum += int(n)**len(digits)
    if sum == number:
        return True
    else:
        return False