import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l1=[]
    m1=max(arr)
    l1.append(m1)
    arr.remove(m1)
    m2=min(arr)
    l1.append(m2)
    arr.remove(m2)
    smin=l1[1]
    for i in range(0,len(arr)):
        smin=smin+arr[i]
    smax=l1[0]
    for i in range(0,len(arr)):
        smax=smax+arr[i]
    l2=[smin,smax]
    for j in range(0,len(l2)):
        print(l2[j],end=" ")
        
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
