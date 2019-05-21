# solution using numpy arrays

import re
import numpy as np

def verify(isbn):
    # remove all other than numbers and X
    isbn_clean = ''.join(re.findall(r'\d+|X$', isbn))
    isbn_split = [n for n in isbn_clean]

    # check validity
    if len(isbn_split) != 10:
        return False
    else:
        if isbn_split[9] == 'X': isbn_split[9] = '10'   # sub 10 for X
        a = np.array([n for n in range(10,0,-1)])       # create multiplier array
        b = np.array([int(n) for n in isbn_split])      # convert isbn digits to array
        if (a.dot(b) % 11 == 0):                        # validate isbn
            return True
        else:
            return False