#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort(reverse=False)
    n = len(arr)
    
    if n%2 == 0:
        q2 = (arr[n//2 -1]+arr[n//2])/2
        L = arr[:n//2]
        U = arr[n//2:]
        n_l = len(L)
        if n_l%2 ==0:
            q1 = (L[n_l//2-1]+L[n_l//2])/2
            q3 = (U[n_l//2-1]+U[n_l//2])/2
        else:
            q1 = L[n_l//2]
            q3 = U[n_l//2]          
    else:
        q2 = arr[n//2]
        L = arr[:n//2]
        U = arr[n//2+1:]
        n_l = len(L)
        if n_l%2 ==0:
            q1 = (L[n_l//2-1]+L[n_l//2])/2
            q3 = (U[n_l//2-1]+U[n_l//2])/2
        else:
            q1 = L[n_l//2]
            q3 = U[n_l//2]
    return int(q1),int(q2),int(q3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    data = map(int, raw_input().rstrip().split())

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
