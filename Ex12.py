import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200, -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])


def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    current = 0
    for coeff in c:
        square_err = sum((y - X @ coeff) ** 2)
        if square_err < smallest_error:
            best_index = current
            smallest_error = square_err
        current += 1
        # edit here: calculate the sum of squared error with coefficient set coeff and
        # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % best_index)


find_best(X, y, c)
