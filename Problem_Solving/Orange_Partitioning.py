'''
Tisha plucked n oranges from her orchard and wants to divide them into three groups:

    1) For her children – all oranges smaller than or equal to the last orange in her hand.

    2) For herself – the last orange in the row (considered special).

    3) For the market – all oranges larger than the last orange.

To do this, she performs the following partitioning algorithm:

    1) Let the last orange (i.e., orange[n-1]) be the pivot orange.

    2) Initialize a pointer k = 0.

    3) For every orange from index 0 to n-2, do:

        -> If orange[i] <= pivot, swap orange[i] with orange[k], then increment k.

    4) After the loop, swap orange[k] with the pivot (orange[n-1]).

Your task is to simulate this partitioning process and print the modified list of orange diameters.
'''


def partition_orange(oranges, num_oranges):

    k = 0
    pivot = oranges[num_oranges - 1]

    for i in range(num_oranges - 1):
        if oranges[i] <= pivot:
            oranges[i], oranges[k] = oranges[k], oranges[i]
            k += 1


    oranges[k], oranges[num_oranges - 1] = oranges[num_oranges - 1], oranges[k]

    return oranges

num_oranges = int(input("Enter the number of oranges: "))
oranges = list(map(int,input("Enter the diameters of oranges: ").split()))

print("Partition of oranges:", partition_orange(oranges, num_oranges))

