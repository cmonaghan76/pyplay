from collections import Counter
import operator

# Score categories
# Change the values as you see fit
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "fh"
FOUR_OF_A_KIND = "4kind"
LITTLE_STRAIGHT = "ls"
BIG_STRAIGHT = "bs"
CHOICE = "choice"


def score(dice, category):
    points = 0
    if category == "ones":
        for die in dice:
            if die == 1:
                points += 1
    elif category == "twos":
        for die in dice:
            if die == 2:
                points += 2
    elif category == "threes":
        for die in dice:
            if die == 3:
                points += 3
    elif category == "fours":
        for die in dice:
            if die == 4:
                points += 4
    elif category == "fives":
        for die in dice:
            if die == 5:
                points += 5
    elif category == "sixes":
        for die in dice:
            if die == 6:
                points += 6
    elif category == "fh":
        values = list(Counter(dice).values())
        if (3 in values) and (2 in values):
            for die in dice:
                points += die
    elif category == "4kind":
        distr = Counter(dice)
        values = list(distr.values())
        if (4 in values) or (5 in values):
            points = 4 * max(distr.items(), key=operator.itemgetter(1))[0]
    elif category == "ls":
        dice.sort()
        n = 1
        for die in dice:
            if die == n:
                n += 1
                points = 30
            else:
                points = 0
                break
    elif category == "bs":
        dice.sort()
        n = 2
        for die in dice:
            if die == n:
                n += 1
                points = 30
            else:
                points = 0
                break
    elif category == "choice":
        for die in dice:
            points += die
    elif category == "yacht":
        distr = Counter(dice)
        if list(distr.values())[0] == 5:
            points = 50
        else:
            points = 0

    return points