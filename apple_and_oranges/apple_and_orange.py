#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s = 7, t = 10, a = 4, b = 12, apples = [2,3,-4], oranges = [3,-2,-4]
    # apples = [4+2,4+3,4+-4], oranges = [12+3,12+-2,12+-4]
    # apples = [6,7,0], oranges = [15,10,8]
    # Write your code here
    
    apples_in_house = 0
    oranges_in_house = 0
    
    for i in range(len(apples)):
        apples[i] += a
        
    for i in range(len(oranges)):
        oranges[i] += b

    # total apples in the house
    for i in range(len(apples)):
        if(apples[i] >= s and apples[i] <= t):
            apples_in_house += 1
    
    # total oranges in the house
    for i in range(len(oranges)):
        if(oranges[i] >= s and oranges[i] <= t):
            oranges_in_house += 1
            
    print(apples_in_house)
    print(oranges_in_house)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
