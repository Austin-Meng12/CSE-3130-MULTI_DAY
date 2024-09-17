# d_selection_sort.py

"""
title: selection sort algorithm
author: Austin Meng
date-created: 2023-02-06

"""
from myFunctions import *
def selectionSort(LIST):
    """
    compares the current index value with the rest of the set.
    It will find the lowest value in the set and place it in
     the lowest index  in the unsorted half of the list



    :param LIST:

    """
    for i in range(len(LIST)-1):    # for each place in the list ( except the last)
        # i is the position being sorted.
        MINIMUM_VALUE_INDEX = i    #assuming index i is the lowest value
        for j in range(i+1, len(LIST)): # each value after i, including the last
            if LIST[j] < LIST[MINIMUM_VALUE_INDEX]:
                # test if the current value is less than the assumed minimum value.

                MINIMUM_VALUE_INDEX = j # update the minimum value index to the current index.
        if LIST[MINIMUM_VALUE_INDEX] < LIST[i]: # test if our minimum value is in the i-th position
            # if not, switch the position with the smallest value
            TEMP = LIST[i]
            LIST[i] = LIST[MINIMUM_VALUE_INDEX]
            LIST[MINIMUM_VALUE_INDEX] = TEMP

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        selectionSort(NUMBERS)
        END = getTime()
        TIMES.append(END-START)
        print(TIMES[-1])
    print(getAverage(TIMES))




