"""
title: Recursive example of Binary Search
author: Austin Meng
date-created: 2023-02-10

"""
from myFunctions import *

def recurBinarySearch(LIST, VALUE):
    """


    :param LIST: (int)
    :param VALUE: int
    :return: bool
    """

    if len(LIST) > 0:
        MIDPOINT = len(LIST) // 2
        if LIST[MIDPOINT] == VALUE:
            # base case
            return True
        else:
            if VALUE > LIST[MIDPOINT]:
                return recurBinarySearch(LIST[MIDPOINT + 1:], VALUE)
            else:
                return recurBinarySearch(LIST[:MIDPOINT], VALUE)
    else:
        return False


if __name__ == "__main__":
    import random
    TIMES = []

    NUMBERS = getList(10000000)
    for i in range(30):
        NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
        START = getTime()
        print(recurBinarySearch(NUMBERS, NUMBER))
        END = getTime()
        TIMES.append(END - START)

    print(getAverage(TIMES))

