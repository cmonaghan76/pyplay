import timeit
from functools import reduce


testnum = 105


def raindrops_optimum(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    raindrops = ''.join([sounds[factor] for factor in sounds.keys() if number % factor == 0])
    if raindrops == '':
        return str(number)
    else:
        return raindrops


def raindrops_oversimplified(number):
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


def raindrops_overcomplicated(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    factors = get_factors(number)
    raindrops = ''.join([sounds[factor] for factor in sorted(factors) if factor in sounds.keys()])
    if raindrops == '':
        return str(number)
    else:
        return raindrops


def get_factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


#print("Raindrops 'Optimum':", timeit.timeit(raindrops_optimum(testnum), number = 100000))
print("Raindrops 'Oversimplified':", timeit.timeit(raindrops_oversimplified(testnum), number = 100000))
#print("Raindrops 'Overcomplicated':", timeit.timeit(raindrops_overcomplicated(testnum), number = 100000))