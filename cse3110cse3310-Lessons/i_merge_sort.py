# i_merge_sort.py

"""
title: merge sort
author: Austin Meng
date-created: feb 13, 2023

"""

from myFunctions import *
def mergeSortedList(LIST_LEFT, LIST_RIGHT):
    """

    :param LIST_LEFT: list(Int)
    :param LIST_RIGHT: list(Int)
    :return: list(Int)
    """
    # Special Case: one or both lists are empty
    if len(LIST_LEFT) ==0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # general case
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGED = [] # list to build and return
    LIST_LEN_TOTAL = len(LIST_LEFT) + len(LIST_RIGHT)


    while len(LIST_MERGED) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
            LIST_MERGED.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT = INDEX_LEFT + 1
        else:
            LIST_MERGED.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT += 1

        # test if we are at the end of one of the lists

        if INDEX_RIGHT == len(LIST_RIGHT):
            LIST_MERGED = LIST_MERGED + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGED += LIST_RIGHT[INDEX_RIGHT:]
            break
    return LIST_MERGED

def mergeSort(LIST):
    """

    recursive split of the Merge Sort
    :param LIST: list(int)
    :return: list
    """


    if len(LIST) <= 1:
        # base case
        return LIST
    else:
        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]
        return mergeSortedList(mergeSort(LEFT), mergeSort(RIGHT))

if __name__ == "__main__":
    TIMES = []

    for i in range(30):

        NUMBERS = getRandomList(10000)
        START = getTime()
        mergeSort(NUMBERS)
        END = getTime()
        print(END - START)
        TIMES.append(END - START)

    print(getAverage(TIMES))
