# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
