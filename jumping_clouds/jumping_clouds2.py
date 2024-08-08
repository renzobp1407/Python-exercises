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
    i = 0
    
    while (i < len(c) - 1):
        
        # validating the index +2 is going to get out of bound
        if(i+2 > len(c) - 1 ):
            if(i+1 == len(c) - 1):
                if (c[i] == 0 and c[i+1] == 0):
                    sum_jumps += 1
                    i += 1            
                elif (c[i] == 0 and c[i+1] == 1):
                    break
        
        # validating the index +1 is going to get out of bound
        if(i+1 > len(c) - 1):
            break

        # jumping on the array of clouds
        if (c[i] == 0 and c[i+1] == 0 and c[i+2] == 0):
            sum_jumps += 1
            i += 2
        elif (c[i] == 0 and c[i+1] == 1 and c[i+2] == 0):
            sum_jumps += 1
            i += 2
        elif (c[i] == 0 and c[i+1] == 0 and c[i+2] == 1):
            sum_jumps += 1
            i += 1

        # This print helps to trace the number of jumps
        print(sum_jumps)

    return(sum_jumps)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
