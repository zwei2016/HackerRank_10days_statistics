#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function

    def median1(dataset2):
        m = len(dataset2)
        if m%2==0:
            return (dataset2[m//2-1] + dataset2[m//2])*1.0/2
        else:
            return dataset2[m//2]
    
            
    dataset = [[v]*f for v,f in zip(values, freqs)]
    dataset1 = []
    
    for li in dataset:
        dataset1.extend(li)
        
    n = len(dataset1)
    dataset1.sort(reverse=False)
    #print(dataset1)
    
    if n%2==0:
        left = dataset1[:n//2]
        right = dataset1[n//2:]
    else:
        left = dataset1[:n//2]
        right = dataset1[n//2+1:]
    
    q3, q1 = median1(right), median1(left)
    
    print(round(q3-q1,1))
    
    

if __name__ == '__main__':
    n = int(raw_input().strip())

    val = map(int, raw_input().rstrip().split())

    freq = map(int, raw_input().rstrip().split())

    interQuartile(val, freq)
