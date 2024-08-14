#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    
    new_factorial = 0
    initial_descending_number = n
    
    for i in range(1, n+1):
        if i == n:
            break        
        if i == 1:
            new_factorial = (n * (n - i))
        else:
            new_factorial = (new_factorial * (n - i))
            


        #print(new_factorial)
        #print(i)
    #return new_factorial
    print(new_factorial)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
