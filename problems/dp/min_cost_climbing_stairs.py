from typing import List

# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 
# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Time -> O(N)
    Space -> O(N)
    """
    n = len(cost)

    if n == 2:
        return min(cost[0], cost[1])

    dp = [0] * (n)
    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1],  dp[i-2])
    
    print(dp)
    return min(dp[n-1], dp[n-2])

def minCostClimbingStairs2(cost: List[int]) -> int:
    """
    Time -> O(N)
    Space -> O(1)
    """

    cost.append(0)

    # iterate in revese from n-3
    for i in range(len(cost)-3, -1,-1):
        cost[i] += min(cost[i+1], cost[i+2])

    print(cost)
    # cost array is guaranteed to have at least 2 values
    return min(cost[0], cost[1])


if __name__ == '__main__':
    cost = [10,15,20]
    output =  15

    cost2 = [1,100,1,1,1,100,1,1,100,1]
    output2 =  6

    print(minCostClimbingStairs(cost) == output)
    print(minCostClimbingStairs(cost2) == output2)

    print(minCostClimbingStairs2(cost) == output)
    print(minCostClimbingStairs2(cost2) == output2)