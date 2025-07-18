import numpy as np
from scipy import stats

if __name__ == '__main__':
    arr = np.array([1,2,2,3,3,3,4,5,6,6,7,7,7,8,8,9,9,9,9])

    mean = np.mean(arr)
    median = np.median(arr)
    res = stats.mode(arr)

    print("Mean: %12.2f" % mean)
    print("Median: %7d" % median)
    print("Mode: %9d" % res.mode)
    print("Mode Count: %3d" % res.count)