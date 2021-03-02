import numpy as np
import random as random


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    x = 0
    seq = []
    for i in range(0, 10000):
        prob = random.random()
        if prob < p1:
            x = 1
        else:
            x = 0
        seq.append(x)
    return seq


def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    cor = 0
    occ = 0
    for i in seq:
        if i is 1:
            cor += 1
        else:
            cor = 0
        if cor >= 5:
            occ += 1

    return occ


def main(p1):
    seq = generate(p1)
    print(seq)
    return count(seq)


print(main(2 / 3))
