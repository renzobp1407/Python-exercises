#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

# output example
# 0 0 1 0 0 1 0  
# 0 1 0 0 1 0

def jumpingOnClouds(c):

    
    sum_jumps = 0
    
    for i in range(len(c)):
         
        # the index is going to get out of bound, breaks
        if(i+2 >= len(c)):
            break
        
        # When the index is equals to the  last value of the list, breaks
        if(i == len(c) - 1):
            if (c[i] == 0 and c[i+1] == 0):
                sum_jumps += 1
                i += 1
                break
        elif (c[i] == 0 and c[i+1] == 1):
            sum_jumps += 1
            i += 2
        elif (c[i] == 0 and c[i+1] == 1 and c[i+2] ==0):
            sum_jumps += 1
            i += 2
        elif (c[i] == 0 and c[i+1] == 0 and c[i+2] == 1):
            sum_jumps += 1
            i += 1
        elif (c[i] == 0 and c[i+1] == 0 and c[i+2] == 0):
            sum_jumps += 1
            i += 2

    return(sum_jumps)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
