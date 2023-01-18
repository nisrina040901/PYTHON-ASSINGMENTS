import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
  al = list(ar) # create a new list al. copy elements in integer array ..
                # ... ar and store in list al .
  count = 0               # to count how many pair that  isi divisible b k 
  for i in range(n) : # increase i by 1 starting from 0 until n 
      for j in range ( i + 1,n): # increase i by 1 starting from i + 1 until n 
          if ((al[i]+al[j])%k == 0) : 
            count += 1
  return count        

  if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = map(int, input().rstrip().split())

    result = divisibleSumPairs(n, k, ar)

    print(result)