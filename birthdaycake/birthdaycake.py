#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    
    max_candle_height = 0
    candles_count = 0
    
    # extracting the tallest number
    for candle in candles:
        if(max_candle_height <= candle):
            max_candle_height = candle
            
    for candle in candles:
       if(max_candle_height == candle):
           candles_count += 1        
           
    return(candles_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))


    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
