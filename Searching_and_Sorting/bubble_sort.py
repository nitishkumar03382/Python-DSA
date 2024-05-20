from os import *
from sys import *
from collections import *
from math import *

def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    pass