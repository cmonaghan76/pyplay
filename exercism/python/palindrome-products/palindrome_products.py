import itertools


def largest_palindrome(max_factor, min_factor=0):
    palindromes = get_palindromes(max_factor, min_factor)
    if len(palindromes) >= 1:
        largest = max(palindromes.keys())
        return (largest, set(palindromes[largest]))
    else:
        return (None,[])


def smallest_palindrome(max_factor, min_factor=0):
    palindromes = get_palindromes(max_factor, min_factor)
    if len(palindromes) >= 1:
        smallest = min(palindromes.keys())
        return (smallest, set(palindromes[smallest]))
    else:
        return (None,[])


def get_palindromes(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be smaller than max_factor")
    palindromes = dict()
    for a, b in itertools.combinations_with_replacement(range(min_factor, max_factor + 1), 2):
        product = str(a * b)
        if product == product[::-1]:
            if int(product) in palindromes.keys():
                palindromes[int(product)].append((a ,b))
            else:
                palindromes[int(product)] = [(a, b)]
    return palindromes