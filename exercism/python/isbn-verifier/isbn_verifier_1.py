# solution using for-loop sum accumulation

import re

def verify(isbn):
    # remove all other than numbers and X
    isbn_clean = ''.join(re.findall(r'\d+|X$', isbn))
    isbn_split = [n for n in isbn_clean]

    # verify correct length
    if len(isbn_split) != 10:
        return False
    else:
        # verify number with checkdigit
        multiplier = 10
        value = 0
        for n in range(0,9):
            value += int(isbn_split[n]) * multiplier
            multiplier -= 1
        if isbn_split[9] == 'X':
            value += 10
        else:
            value += int(isbn_split[9])
        
    # perform mod 11, and return validity
    if value % 11 == 0:
        return True
    else:
        return False