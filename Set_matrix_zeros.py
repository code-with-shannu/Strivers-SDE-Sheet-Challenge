from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    #row = [0]*len(matrix)
    #col = [0]*len(matrix[0])
    col0=1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0 = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]==0
    if matrix[0][0]==0:
        for j in range(len(matrix[0])):
            matrix[0][j]=0
    if col0==0:
        for i in range(len(matrix)):
            matrix[i][0]=0
    pass
