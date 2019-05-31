def is_isogram(string):
    string = string.lower().translate({ord(i):None for i in ' -'})
    duplicates = [letter for letter in string if string.count(letter) > 1]
    if duplicates:
        return False
    else:
        return True