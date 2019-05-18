# Solution by Christopher Monaghan for exercism.io python track
# May 17, 2019

def slices(series, length):
    if (length < 1):
        raise ValueError('Length argument must be greater than 0')
    elif (length > len(series)):
        raise ValueError('length argument must be less than the series length')
    else:
        substrings = list()
        len(series)
        n = 0
        while n < (len(series) - (length - 1)):
            substrings.append(series[n:length+n])
            n += 1
        return substrings