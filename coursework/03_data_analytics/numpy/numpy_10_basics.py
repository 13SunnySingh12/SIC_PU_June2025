# Building an array from a function of its indices with np.fromfunction, then
# using slice assignment to zero out the whole border in two statements.

import numpy as np

def f(x, y):
    return 10 * x + y

if __name__ == '__main__':
    array = np.fromfunction(f, (5, 4), dtype=float)
    print(array)

    array[:, [0, -1]] = 0
    array[[0, -1], :] = 0

    print(array)

