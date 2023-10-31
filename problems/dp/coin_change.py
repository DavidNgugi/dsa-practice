from typing import List

# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


def coinChange(coins: List[int], amount: int) -> int:
    """
    Bottom-Up DP Approach
    How many coins sum to 0 -> 11
    Time -> O(A*N) where A is the amount and N the number of coins
    Space -> O(N) N results
    """

    if amount == 0:
        return 0

    minCoins = [float("Inf")] * (amount + 1)
    minCoins[0] = 0
    print("created", minCoins)

    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                print("minCoins[i] i", i, "->", minCoins[i])
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    print("completed", minCoins)

    if minCoins[amount] == float("Inf"):
        return -1

    return minCoins[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    output = 3

    coins2 = [2]
    amount2 = 3
    output2 = -1

    coins3 = [1]
    amount3 = 0
    output3 = 0

    print(coinChange(coins, amount) == output)
    print(coinChange(coins2, amount2) == output2)
    print(coinChange(coins3, amount3) == output3)
