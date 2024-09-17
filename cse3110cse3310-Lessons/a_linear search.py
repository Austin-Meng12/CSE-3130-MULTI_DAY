"""
title: Linear Search
name: Austin Meng
date-created: 2023-02-02
"""

import random
import time
import statistics
# Make a large data set
NUMBERS = []
for i in range(20000000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)
TIMES = []
for i in range(30):
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
    print(NUMBER)


# search for VALUE
START_TIME = time.perf_counter()

for i in range(len(NUMBERS)):
    if NUMBERS[i] == NUMBER:
        print("found!")
        break  # stops the rest of the for loop
    END_TIME = time.perf_counter()
TIMES.append(END_TIME - START_TIME)
print(statistics.mean(TIMES))
