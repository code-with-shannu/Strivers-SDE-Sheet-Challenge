def maximumProfit(prices):
    # Write your code here.
    curr_min = prices[0]
    ans = float('-inf')
    for i in range(1,len(prices)):
        if prices[i]>curr_min:
            ans = max(ans,prices[i]-curr_min)
        else:
            curr_min=prices[i]
    if ans==float('-inf'):
        return 0
    else:
        return ans
#T.C =O(N)