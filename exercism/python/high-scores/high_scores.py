# Solution by Christopher Monaghan for exercism.io python track
# May 17, 2019

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores, reverse=True)[0]


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
