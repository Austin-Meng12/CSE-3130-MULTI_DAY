# g_recursive_linear_search.py
"""
Title: recursive linear search
author: Austin Meng
date-created: 2023 - 02 -09
"""

from myFunctions import *

def recurLinearSearch(LIST, VALUE):
    """

    Search linearly through the list to find a value
    :param LIST: list (int)
    :param Value: int
    :return: bool
    """
    if LIST[0] == VALUE:
        return True
    else:
        return recurLinearSearch(LIST[1:], VALUE)


if __name__ == "__main__":
    import random

    TIMES = []
    for i in range(30):

        NUMBERS = getList(1000)
        NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
        START = getTime()
        print(recurLinearSearch(NUMBERS, NUMBER))
        END = getTime()
        TIMES.append(END - START)

    print(getAverage(TIMES))
    