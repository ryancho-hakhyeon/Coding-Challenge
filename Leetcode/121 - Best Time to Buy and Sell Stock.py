from typing import List


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r += 1

        return res


ob = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(ob.maxProfit(prices))     # Output: 5
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [7, 6, 4, 3, 1]
print(ob.maxProfit(prices))     # Output: 0
# In this case, no transactions are done and the max profit = 0.