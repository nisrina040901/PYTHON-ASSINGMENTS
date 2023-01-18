import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
   maxheight = max(height)  
   
   dose = maxheight - k 
   return max(dose,0)
   
if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

# n is total number of hurdles 
    n = int(first_multiple_input[0])

# max unit that Dan can jump 
    k = int(first_multiple_input[1])

#value of each hurdles 
    height = map(int, input().rstrip().split()) # using map to change all entered input to ...
                                                # .... integer and store in ....
                                                # .... integer array height for 
                                                # .... calculator later 
    result = hurdleRace(k, height)

    print(result)