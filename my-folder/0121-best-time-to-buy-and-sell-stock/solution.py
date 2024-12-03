class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize the minimum price as infinity
        max_profit = 0  # Initialize the maximum profit to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update the maximum profit

        return max_profit

