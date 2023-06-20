'''In a brute force manner we have to iterate with each element and traverse the whole array and find the maximum sum
But this takes a time complexity of O(N^2)
So the optimised is carry forward + sliding window technique. We will traverse through the array.
for each element we add to the current maximum so far and check whether the sum is greater than previous or not
the maximum is stored in the current and then we will check this current with the max_so_far and store the max in maximum_so_far
this takes a T.C of O(N) and S.C O(1) 
'''


def maxSubarraySum(arr, n):
    max_so_far = 0
    curr_max = 0
    for i in range(n):
        curr_max = max(arr[i],curr_max+arr[i])
        max_so_far = max(max_so_far,curr_max)
    return max_so_far
