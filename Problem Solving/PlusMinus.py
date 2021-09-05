import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print(round((pos/len(arr)),6))
    print(round((neg/len(arr)),6))
    print(round((zero/len(arr)),6))     
            

    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

    
    
    
OUTPUT
Input (stdin)
6
-4 3 -9 0 4 1
Your Output (stdout)
0.5
0.333333
0.166667
Expected Output

Download
0.500000
0.333333
0.166667
