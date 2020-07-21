# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        min_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # TO-DO: swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# test the function
arr = [5, 55, 6, 67, 16, 9, 25, 43, 12]
print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # set up a nested for loop
    for j in range(len(arr)):
        # for each loop, check each # against the # to its right
        for i in range(len(arr) - 1):
            # if the # to the right is less than, swap the two
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


arr = [5, 55, 6, 67, 16, 9, 25, 43, 12]
print(bubble_sort(arr))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
