#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
def aVeryBigSum(ar):
    # Write your code here
    
    result_long_int = 0
    
    for i in range(len(ar)):
        
        result_long_int = result_long_int + ar[i]


    return(result_long_int)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
