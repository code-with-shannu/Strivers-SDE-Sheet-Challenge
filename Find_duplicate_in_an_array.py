
def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    slow = arr[arr[0]]
    fast = arr[arr[arr[0]]]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    fast = arr[0]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow