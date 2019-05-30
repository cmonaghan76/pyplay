def raindrops(number):
    sounds = ""
    if number % 3 == 0:
        sounds = sounds + "Pling"
    if number % 5 == 0:
        sounds = sounds + "Plang"
    if number % 7 == 0:
        sounds = sounds + "Plong"
    if sounds == "":
        sounds = str(number)
    return sounds