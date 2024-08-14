#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    
    complete_time_word = ''
    hours_to_letters = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    minutes_to_letters = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight','twenty nine']
    
    
    
    if m == 0:
        complete_time_word = hours_to_letters[h] + " o' clock"
    elif m == 1:
        complete_time_word = 'one minute past ' + hours_to_letters[h]
    elif m == 15:
        complete_time_word = 'quarter past ' + hours_to_letters[h]
    elif m == 30:
        complete_time_word = 'half past ' + hours_to_letters[h]
    elif m == 45:
        complete_time_word = 'quarter to ' + hours_to_letters[h+1]
    elif m > 1 and m < 15 or m > 15 and m < 30:
        complete_time_word = minutes_to_letters[m] + ' minutes past ' + hours_to_letters[h]
    elif m > 30 and m < 45 or m > 45 and m < 60:
        complete_time_word = minutes_to_letters[60 - m] + ' minutes to ' + hours_to_letters[h+1]
    
    return(complete_time_word) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
