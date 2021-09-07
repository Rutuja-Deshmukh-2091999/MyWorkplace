import math
import os
import random
import re
import sys


def timeConversion(s):
    h=int(s[0:2])
    
    if s[-2]=='P' or s[-2]=='p':
        if h!=12:
            h=12+h
        else:
            h=h    
        return(str(h)+s[2:8])
    else:
        if h==12:
            return("00"+s[2:8])
        else:
            return(s[:8])

    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

