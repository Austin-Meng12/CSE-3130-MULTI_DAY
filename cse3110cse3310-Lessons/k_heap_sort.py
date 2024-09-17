# k_heap_sort.py

"""
title: heap sort
author: Austin Meng
date-created: 2023 - 02 - 16
"""

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """

    Heapifies all subtrees in the binary tree
    :param LIST: list(int)
    :param LEN_ARRAY: int - length of the array
    :param ROOT_INDEX:  int - parent index
    :return: none
    """

    LARGEST_INDEX = ROOT_INDEX # assuming root index is the largest
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2
    # test if left child value is larger than the largest index value
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # test if right child value is larger than the largest index value
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX


    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP


        # heapify the ROOT
        heapify(LIST,LEN_ARRAY, LARGEST_INDEX)



def heap_sort(LIST):
    """

    Sort the list
    :param LIST: list(int)
    :return: none
    """
    LEN_ARRAY = len(LIST)
    # build a max heap
    for i in range(LEN_ARRAY-1, -1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # Extract the highest value in the heap and recur
    for i in range(LEN_ARRAY - 1, 0, -1):
        LIST[i], LIST[0] = LIST[0] , LIST[i]
        heapify(LIST, i , 0)


if __name__ == "__main__":
    from myFunctions import *
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        heap_sort(NUMBERS)
        END = getTime()
        print(END - START)
        TIMES.append(END-START)

    print(getAverage(TIMES))
