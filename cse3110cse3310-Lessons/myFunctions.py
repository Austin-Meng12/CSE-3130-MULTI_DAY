# myFunctions.py

"""
title: common functions for all sort algorithms
author: Austin Meng
date - created: 2023-02-03
"""

import random, time, statistics

def getSmallList():
    """


    :return:
    """
    return[5, 1, 19, 1, 11, 17, 7, 13]

def getList(SIZE):
    """

    :param SIZE:
    :return:
    """
    NUMBERS = []

    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def getRandomList(SIZE):
    """
    return a randomized list of approximately Size size

    :param SIZE:
    :return:
    """
    SORTED_LIST = getList(SIZE)
    RANDOM_LIST = []
    for i in range(len(SORTED_LIST)):
        RANDOM_LIST.append(SORTED_LIST.pop(random.randrange(len(SORTED_LIST))))


    return RANDOM_LIST


def getAverage(TIMES):
    """
      return the average of the given list

      :param SIZE:
      :return:
      """

    return statistics.mean(TIMES)

def getTime():
    """
    returns the performace counter


    :return:
    """
    return time.perf_counter()