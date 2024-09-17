# c_bubble_sort.py
"""
title: bubble sort
author: Austin Meng
date-created: 2023 - 02 -03

"""
from myFunctions import *

def bubbleSort(LIST):


    """
        compares the two adjacent values and moves the highest one to the end of the list.

    :param LIST:
    :return: NUMBER(int)
    """
    for i in range(len(LIST) - 1, 0, -1):  # transverses backwards from end to index 1.
        for j in range(i):  # transverses forward in the unsorted section
            # check to switch two current values
            if LIST[j] > LIST[j+1]:
                TEMP = LIST[j]
                LIST[j] = LIST[j+1]
                LIST[j+1] = TEMP

if __name__=="__main__":
    #NUMBERS = [5, 1, 19, 1, 11, 17, 7, 13]
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        bubbleSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(END - START)

    print(getAverage(TIMES))


