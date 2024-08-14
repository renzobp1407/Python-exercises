#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# 4
# 2 5 3 1

# 1 2 3 5

def lilysHomework(arr):
    # Write your code here
    
    def total_list_swaps(arr, target):

        position_list_values = {value: i for i, value in enumerate(arr)}
        number_of_swaps = 0
    
        for i in range(len(arr)):
    
            if arr[i] != target[i]:
                number_of_swaps += 1
    
                swap_index = position_list_values[target[i]]
                
                position_list_values[arr[i]] = swap_index
                
                arr[i], arr[swap_index] = arr[swap_index], arr[i]
    
        return number_of_swaps
    
    
    arr_original_copy = arr[:]
    
    sorted_array = sorted(arr)
    ascended_swaps = total_list_swaps(arr[:], sorted_array)
    
    
    sorted_array_reverse = sorted(arr, reverse=True)
    descended_swaps = total_list_swaps(arr_original_copy, sorted_array_reverse)
    
    
    return min(ascended_swaps, descended_swaps)    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
