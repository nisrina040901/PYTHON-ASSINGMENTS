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
    # Write your code here
    # for every applle [i] + that is between s and t , then count = 1 for apple 
    print(sum([1 for i in apples if s <= (i + a ) <= t ]))
    # for every ornage [j] + b that is between s and t , then count +1 for orange
    print(sum([1 for j in oranges if s <= (j + b ) <= t ]))

# it allows you to exucates code when the files runs as a script
if __name__ == '__main__':
    # asking area of Sam's house , s and t 
    # rstip() method removes any trailing characters (characters at the ......)
    # split () method splits a strings into a list , default separator is any ....
    # .... whitespaces 
 
    first_multiple_input = input().rstrip().split()
    # left side of Sam's house 

    s = int(first_multiple_input[0])

    # right side of Sam's house
    t = int(first_multiple_input[1])


    #asking input a and b 
    # rstript () method removes any trailing characters ( characters to remove ....)
    # .... split () method splits a string into a list default separator is any ....
    # .... whitespace 

    second_multiple_input = input().rstrip().split()

    # location of apple tree 
    a = int(second_multiple_input[0])

    # locaton of orange tree 
    b = int(second_multiple_input[1])

    # asking input m and n
    # rstript () method removes any trailing characters ( characters at the end a string ), space is the default 
    # split () method splits a string into a list , default separator is any whitespace . 
    third_multiple_input = input().rstrip().split()

    # total number of fallens applle 
    m = int(third_multiple_input[0])
    # total number of fallens oranges
    n = int(third_multiple_input[1])

    # asking distance of each apple from the tree 
    # rstrip () method removes any trailing characters (characters at the end a string ), space 2is the default 
    # split () method splits a string into a list, default separator is any whitespaces 
    fourth_multiple_input = input().rstrip().split
    apples = map(int, input().rstrip().split())

  #asking distance of each orange from the tree
  # rstrip() method removes any trailing characters (characters at the end a string ) . space is the default 
  # split() method splits a string into a list , default separator is any whitespaces  

    oranges = map(int, input().rstrip().split()) # change all elements on fifth_multiple_input into integer and  

    countApplesAndOranges(s, t, a, b, apples, oranges)