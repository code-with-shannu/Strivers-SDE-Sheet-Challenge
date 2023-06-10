'''Problem Statement:
    You are given an array of size N containing only zeros and ones. you should return the sourted array.
Sample Input 1 :
2
6
0 1 2 2 1 0
7
0 1 2 1 2 1 2
Sample Output 1 :
0 0 1 1 2 2
0 1 1 1 2 2 2
Sample Input 2 :
2
7
2 2 2 1 1 1 0
6
2 1 2 0 1 0
Sample Output 2 :
0 1 1 1 2 2 2
0 0 1 1 2 2
'''
'''
Brute Force:
We can use any of the sorting algorithms to solve this problem and takes a time complexity of O(NlogN)

Better :
Instead of sorting, we can maintain a counter for 0,1,2 and then we can append those many zeros & ones and twos to the array
This executes in O(N) and S.C = O(1)
Although in this approach we are traversing through the array two times so T.C is most accurately O(2N)

'''


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    zeros = 0
    ones = 0
    twos = 0
    for i in arr:
        if i==0:
            zeros+=1
        elif i==1:
            ones+=1
        elif i==2:
            twos+=1
    for i in range(zeros):
        arr[i] = 0
    for i in range(zeros,zeros+ones):
        arr[i] = 1
    for i in range(zeros+ones,zeros+ones+twos):
        arr[i] = 2
    return 
	# write your code here
    # don't return anything 
    pass


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)

'''
Optimal Approach:
Dutch National Flag Algorithm:
In this algorithm we maintain three pointers-->low,mid,high
which points in the array as [0,low-1]-->should consist of zeros
[low, mid-1]--> ones
[high+1, n-1]-->twos
the above three parts of the array are sorted and the only part which is unsorted is [mid,high]
so now we traverse through the array and initially we maintain low,mid = 0 and high = n-1
    if element=0, we know that it should be in range of [0,low-1] so we swap elements at low and mid.Then increment mid,low by 1
    if element=1, we know that it should be in range of [low,mid-1] so it is in the correct range so we wont change anything and increment mid by 1
    if element=2, we know that it should be in range of [high+1,n-1] so we swap elements at high and mid.Then decrement high by 1

In this way in one iteration we are arranging all the elements of the array 
T.C = O(N)
S.C = O(1)
    
    
    
'''