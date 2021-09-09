import math
import os
import random
import re
import sys

def minmax(arr):
    arr.sort()
    print(sum(arr[:-1]),(sum(arr[1:])))

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    minmax(arr)
