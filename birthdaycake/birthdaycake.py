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

 if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
     #count candles and remove whitespaces
     candles_count = int(input().strip())
 
     #put every candle number in a list, removing the last one and spliting, each number with an int value
     candles = list(map(int, input().rstrip().split()))
 
     i = 0
     bigger_number = 0
     candles_total = 0

     #Counting biggest number in candles array
     for x in range(len(candles)):
       if(bigger_number < candles[i]):
         bigger_number = candles[i]
       print(candles[i])  

     #counting each biggest number in array
     for x in range(len(candles)):
       if(bigger_number == candles[i]):
         candles_total = candles_total + 1
 
 
     result = print(candles_total)
 
     fptr.write(str(result) + '\n')
 
     fptr.close()
