# Mean-centring and z-score normalisation: rescaling an array so it has mean 0
# and standard deviation 1, the usual preparation step before modelling.

import numpy as np

if __name__ == '__main__':

    arr = np.random.randint(0, 10, size=(5, 5))
    print("Original Array:\n", arr)


    mean_centered = arr - np.mean(arr)
    print("\nMean-Centered Array:\n", mean_centered)


    std_dev = np.std(arr)
    print("\nStandard Deviation: ", std_dev)


    normalized = (arr - np.mean(arr)) / std_dev
    print("\nZ-score Normalized Array:\n", normalized)
