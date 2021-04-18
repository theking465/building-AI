import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)

    for i in range(N):
        for j in range(N):
            if i is j:
                dist[i][j] = np.inf
                continue
            sum = 0
            for k in range(len(data[i])):
                sum += abs(data[j][k] - data[i][k])
            dist[i][j] = sum
    print(np.unravel_index(np.argmin(dist), dist.shape))


find_nearest_pair(data)
