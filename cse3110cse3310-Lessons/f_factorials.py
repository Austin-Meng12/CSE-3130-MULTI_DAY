#  f_factorials.py
'''
title: Factorials with recursian
author: Austin Meng
date-created: 2023-02-09
'''

def recursiveFactorial(NUMBER):

    """
    calculate the factoiral of the given number

    :param NUMBERS: int
    :return: int
    """

    if NUMBER == 0:
        # base case
        return 1
    else:
        return NUMBER * recursiveFactorial(NUMBER - 1)


def iterativeFactorial(NUMBER):
    """
    :param NUMBER: int
    :return: int
    """
    NUM = 1
    for i in range(1, NUMBER + 1):
        NUM *= i
    return NUM

if __name__ == "__main__":
    NUM = int(input("Enter a Number:"))

    if NUM < 0:
        print("Sorry, factorials don't exist for negative numbers.")
    else:
        FACTORIAL = iterativeFactorial(NUM)
        print(f"The factorial of {NUM} is {FACTORIAL}.")



