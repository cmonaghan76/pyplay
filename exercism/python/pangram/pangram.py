def is_pangram(sentence):
    pangram = True
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in alphabet:
        if letter not in list(sentence.lower()):
            pangram = False
            break
    return pangram