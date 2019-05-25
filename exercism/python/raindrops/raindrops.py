from functools import reduce


def raindrops(number):
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