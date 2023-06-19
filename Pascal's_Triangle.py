
def findrow(row):
    temp = []
    res = 1
    for i in range(1,row+1):
        temp.append(res)
        res = res*(row-i)
        res = res//i    
    return temp

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans = []
    for i in range(n):
        ans.append(findrow(i+1))
    return ans

#T.C = O(N^2)