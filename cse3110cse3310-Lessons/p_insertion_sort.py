#  e_insertion_sort.py

"""
Title: insertion sort algorithm
author: Austin Meng
date-created: 2023 - 02 -08

"""

from myFunctions import  *

def insertSort(LIST):
    """
    takes the lowest value in the unsorted half of the list and
    inserts it into the relative position within the sorted list
    :param LIST:
    :return:
    """
    for i in range(1, len(LIST)):
        INDEX_VALUE =  LIST[i] # saving the VALUE of the lowest index in the unsorted section of the list
        SORTED_INDEX = i - 1 # identify the largest index of the sorted section of the list

        while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            # while traversing tail-to-head in the sorted section
            LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX]
            # overwrite the right value
            SORTED_INDEX = SORTED_INDEX - 1  # move one to the left
            # STOP when SORTED_INDEX reaches 0 or the LIST[SORTED_INDEX] is smaller than the INDEX_VALUE

        LIST[SORTED_INDEX + 1] = INDEX_VALUE  # Replace the SORTED INDEX position with the INDEX VALUE
        # NOTE: One is added to the SORTED_INDEX to adjust for the minus one at the end of the while loop.
if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        insertSort(NUMBERS)
        END = getTime()
        TIMES.append(END-START)
        print(TIMES[-1])
    print(getAverage(TIMES))



