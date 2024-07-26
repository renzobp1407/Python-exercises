#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # cat1 x=1 , cat2 y=2, mouse z=3
    
    cat_a_distance_to_mouse = abs(z - x)
    cat_b_distance_to_mouse = abs(z - y)
    
    if (cat_a_distance_to_mouse == cat_b_distance_to_mouse):
        cat_mouse_string = "Mouse C"
    elif (cat_a_distance_to_mouse < cat_b_distance_to_mouse):
        cat_mouse_string = "Cat A"
    elif (cat_b_distance_to_mouse < cat_a_distance_to_mouse):
        cat_mouse_string = "Cat B"
    
    return(cat_mouse_string)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
