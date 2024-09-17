# b_binary_search.py

"""
title:binary search
name: Austin Meng
date-created: 2023-02-02

"""
from random import randrange
from time import perf_counter
import statistics

def createArray(SIZE:int=10000):
    """
    Create and ordered list of random numbers
    :para, SIZE: Int
    :return: LIST (int)
    """

    NUMBERS = []
    for i in range(2*SIZE):
        if randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def binarySearch(LIST, VALUE):
    """
    :param LIST: List (int)
    :param VALUE: int
    :return: bool
    """

    SMALL_IND = 0
    LARGE_IND = len(LIST) - 1

    while SMALL_IND < LARGE_IND:
        MIDPOINT_IND = (SMALL_IND + LARGE_IND) // 2
        if LIST[MIDPOINT_IND] == VALUE:
            return True
        elif VALUE > LIST[MIDPOINT_IND]:
            SMALL_IND = MIDPOINT_IND + 1
        else:
                LARGE_IND = MIDPOINT_IND

    return False

if __name__ =="__main__":
    NUMBERS = createArray(10000000)
    TIMES = []
    for i in range(30):
        NUMBER = NUMBERS[randrange(len(NUMBERS))]


        START = perf_counter()
        print(binarySearch(NUMBERS, NUMBER))
        END = perf_counter()
        TIMES.append(END - START)

print(statistics.mean(TIMES))







