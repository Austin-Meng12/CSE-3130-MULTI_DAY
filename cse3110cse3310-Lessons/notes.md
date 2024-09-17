# notes.md

# cse3110 - iterative algorithms

Iterative algoritms are algoritms that use loops to process large sets of data. This includes while loops and for loops. IN contrast, recursive algoritms are algoritms that call the same algoritm over and over again to process large sets of data. iterative algorithms thend to be easeier to design, but may increase efficient when using recurisive algoritms

iterative algoritms are easily shown in search and sort algoritms

### Linear search

Linear search is the easiest to program, but least efficient meth of search. It processes the data line-by-line, simlar to brute force decryption algoritms when cracking passwords.

```python
FOUND  = False
for i in range(len(LIST)):
    if VALUE == LIST[i]:
    FOUND = True
    break
```
Linear Search processing time is dependent on the length of the array and the value's placement in the array. Array that are 10000 indices or higher can have a noticable time requirement to process

#### Measuring Times

to measure processing times, the ```time.perf_counter()``` will meausre the approximate milliseconds it takes to run the program

for more accurate results, we use the average of at least 30 trials and then use ```statistics.means()``` to find the average.

### Binary Search

Binary search follows the _divide and conquer_ technique of finding a value. It takes and __ordered__ set of data and tests the midpoint. THen it cuts the list in half and reruns the process.

__ Steps for Binary Search__
1. Determine the Midpoint of the list.
2. Test if the Midpoint is the found value
   1. If the Midpoint is the found value, end.
   2. If the value is larger than the midpoint, redefine the lowest value of the list to be one above the midpoint
   3. If the value is smaller than the midpoint, redefine the larger value of the list to be one below the midpoint.
3. Repeat until the value is found.

* Advantage of Binary Search
  * It is significantly faster than linear search
* Disadvantage of Binary Search
  * List must be already be sorted from smallest to largest
  * List must only contain integers or floats
  * Harder to program

## Sorting Data

just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort algorithms including bubble, selection, insertion, and merge. (python uses Timsort, which is a hybrid of merge and insertion sort designed by Tim Peters in 2002.)

### bubble sort

Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pair and repeats until it reaches the end of the unsorted list. The final index is the values that is sorted and the algorithm repeats until each index (traversed tail to head) is sorted.

NOTE: sort algorithms separate the list into a sorted and unsorted section when referencing the progression of the sort algorithm. WIth each iteration of the sort, one value in unsorted section is placed into the sorted section.
 
Advantages of bubble sort include that it is relatively easy to program and takes less memory; the disadvantage include long processing time directly proportional to the length of the data set. However, the set is often fully sorted before the last iteration

| 1   | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|-----| --- | --- | --- | --- | --- | --- | --- |
| 1   | 3 | 5 | 11 | 17 | 7 | 13 | __19__|
| 1   | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1   | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1   | 3 | 5 | 7 | __11__ | 13 | 17 | 19 |
| 1   | 3 | 5 | __7__ | 11 | 13 | 17 | 19 |
| 1   | 3 | __5__ | 7 | 11 | 13 | 17 | 19 |
| 1   | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |





NOTE: For the unit exam, you may be asked information from a specific iteration of the algorithm

### Selection Sort

Selection sort compares the current index value with the rest of the set. It will find the lowest value and switch positions with the lowest index position of the unsorted half of the list. As it runs through the data, set, it will select the lowest value and place it in the lowest position on the unsorted section of the list

| 1       | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---------| --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1       | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1       | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1       | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1       | 3 | 5 | 7 | __*11*__ | 17 | 19 | 13 |
| 1       | 3 | 5 | 7 | 11 | __13__ | 19 | _17_ |
| 1       | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |

ASIDE: ( Asides are not in an exam) When comparing similar algorithms, measuring the best, worst, and average case scenarios will provide a clearer relationship between the two algorithms

### Insertion sort
Insertion sort splits the list into two sections: sorted and unsorted. As it progresses through the list, it takes the value at the lowest intdex of the unsorted half and inserts it into the correct _relative_ location in the sorted section of the list. The list is only fully sorted, where all values are in the appropriate index location after the final iteration.

| 1       | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---------| --- | --- | --- | --- | --- | --- | --- |
| 1 | __*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ |  11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __11__ | _19_ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | __17__| _19_ | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | _19_ |



# CSE3310 - Recursive Algorithms


A__recursive algorithms__ calls itself with smaller or simpler input values. Recursive algorithms rely on a _base case_, which is the simplest input values. Then there are subprocesses that simplifies more complex input values and returns the simplified values to the _same function_.

Note: All iterative algorithms can be written recursively and vice versa; however certain functions are easier to write in one form over another.

## example 1: testing for correct input


``` python
# iterative
def checkInt(NUMBERS):
    while True:
        if _NUMBER.isnumeric():
            return int(NUMBERS)
        else:
            print("you did not enter a number")
            NUMBERS = input(" Please enter a number: ")
# recurisve
def checkInt(NUMBERS)
    if NUMBERS.isnumberic():
        return int(NUMBERS) # base case
    else:
    #  subprocess to simplify the input value
        print("You did not enter a number")
        return checkInt(input("PLease enter a number: "))
        
```





## Iteration vs. Recursion 
In general, iterative algorithms require more lines of code and more variables than recursive algorithms. It relies on while and for loops to complete the process. One iteration of an iterative algorithm is one loop through the while or for loop. Whereas recursive algorithms do not use as many variables or for loops because return values are re-entered into a _new instance_ of the same function. Therefore, recursions requires more physical memory (RAM) than iterative algorithms because each instance of the recursive function stays in memory until the base case is achieved. In recursion, one instance of the function is one interation of the recursive function. 

## Example 2: Factorials

### Calculate 7!
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1

but!

6! = 6 * 5 * 4 * 3 * 2 * 1

thus, 
7! = 7 * 6!

Continuing the pattern,

7! = 7 * (6 * ( 5 * (4 * (3 * (2 *(1))))))
    
Threfore, we can general factorials as,
```
f(x)  = x * f(x-1), x > 1  -----> suprocess to simplyf the input
      = 1, x = 1 --> base case

```

## Sorting
Recursive sorting uses both recursive and iterative processes in the algorithm. (algorithms use for/while loops and return the function or a sub-function). In general, these hybrid sorts are exponentially faster with longer list. (They are measured on the logarithmic scale).

### Merge Sort
Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then rebuilds the list by combining progressively larger sorted lists together. The recursive portion is the splitting of the list and the iterative portion is the actual merging of the two smaller sorted list together.

Oftentimes, this function is separated into splitting and merging functions

### Quick Sort

Quick sort (quicksort) is another divide and conquer method of sorting. Quicksort utilizies an arbitrary value as its pivot, which is then used to place the pivot value in the correct place in the array. IT does this by placing all smaller values to the left of the pivot and all larger values to the right of the pivot. Then it places the pivot value where the smaller value and larger portion intersects. Then it moves to the next pivot value, recurring until a sublist is a length of one.

NOTE: Quick Sort's efficiency is from separating the list into two sections that will never compare values with each other again.


### Heap sort

heap sort uses a binary tree organization of an array to sort higher values to the top of the tree (lower indexes of the array). Note that while this algorithm represents the numbers in a binary tree, they are still stored in an array. The process of moving larger values higher in the binary tree is called __heapifying__ (to heapify).

To build the binary tree, each index (starting at 0), will have a left child and a right child (hence, binary tree). The index value can be calculated from the following

```
left_child_index = 2 * parent_index + 1
right_child_index = 2 * parent_index + 2

// sample Tree
LIST = [5, 17, 13, 11, 1, 7, 3]

        5[0]
       /    \
    17[1]   13[2]
    /  \      / \
 11[3] 1[4] 7[5] 3[6]
```
To heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom of the tree and works its way to the top. If the parent is smaller than one of the children values, it swaps the highest child value with the parent value. As heapifying moves throughout the tree, the higher values will progressively move to the top.

When heapifying process reaches the top, the tree is in _Max Heap_, where every parent-child group has the larges number as the parent. Then the top value is removed (and placed at the end of the array), and the value from the highest index (at the bottom of the tree) replaces its position at the top. Then the heapifying process begins again.
