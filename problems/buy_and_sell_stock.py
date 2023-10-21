# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:


# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    Time -> O(n)
    Space -> O(1)
    """

    n = len(prices)

    if n == 1:
        return 0

    max_profit = 0

    left = 0

    right = 1

    while right < n:
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(current_profit, max_profit)
        else:
            left = right

        right += 1
    return max_profit


def maxProfitTwoNaive(prices):
    """
    :type prices: List[int]
    :rtype: int
    Time -> O(n)
    Space -> O(n)
    """
    n = len(prices)

    if n == 1:
        return 0

    # check if previous trades are greater than current
    # if greater, keep those in stack
    # else, clear stack and push new profit

    left = 0
    right = 1
    profits = []

    buy_sell_table = {}

    while right < n:
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            print("{}-{}={}".format(prices[right], prices[left], current_profit))
            if left not in buy_sell_table:
                buy_sell_table[left] = current_profit
            if len(profits) > 0:
                sum_prev_profits = sum(profits)
                if sum_prev_profits < current_profit:
                    profits = []
                    if left in buy_sell_table and buy_sell_table[left] < current_profit:
                        buy_sell_table[left] = current_profit
                    profits.append(current_profit)
                else:
                    left = right
            else:
                profits.append(current_profit)
        else:
            left = right
        right += 1

    return sum(buy_sell_table.values())


def maxProfitTwoNaive2(prices):
    """
    Time -> O(n)
    Space -> O(1)
    """
    n = len(prices)

    if n == 1:
        return 0

    profit = 0

    for i in range(n - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
