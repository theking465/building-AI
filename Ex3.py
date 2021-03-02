import math
import random  # just for generating random mountains

# generate random mountains

w = [.05, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in
     range(100)]


def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True  # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1  # right is higher, go there
            summit = False  # and keep going
        elif checkRugged(x, h):
            x = setRugged(x, h)
            summit = False
    return x


def checkRugged(x, h):
    for i in range(x - 5, x + 6):
        if x < 0: continue
        if h[i] > h[x]: return True
    return False


def setRugged(x, h):
    new_x = x
    for i in range(x - 5, x + 5):
        if i < 0 or i > 99: continue
        if h[i] > h[new_x]: new_x = i
    return new_x


def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x


main(h)
