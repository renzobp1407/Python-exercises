#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    # 10 5 20 20 4 5 2 25 1
    # 3 4 21 36 10 28 35 5 24 42
    
    high_score = scores[0]
    low_score = scores[0]
    break_high_record = 0
    break_low_record = 0
    record_break = [1, 2]
    
    for i in range(len(scores)):
        
        
        if(scores[i] > high_score):
            high_score = scores[i]
            break_high_record +=1
            record_break[0] = break_high_record
            
        if( scores[i] < low_score):
            low_score = scores[i]
            break_low_record += 1
            record_break[1] = break_low_record
            
        if(scores[0] == low_score and i == len(scores) - 1):
            record_break[1] = 0
            
        if(scores[0] == high_score and i == len(scores) - 1):
            record_break[0] = 0
            
    return(record_break)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
