class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        if prices.index(min(prices)) < prices.index(max(prices)):
            return max(prices) - min(prices)

        highest_total = max(prices)
        profit = 0

        # if 0 in prices:
        #     profit = max(prices[prices.index(0):])

        for price in prices:
            if highest_total - price > profit:
                highest = max(prices[prices.index(price):])
                if highest == 0:
                    break
                if highest - price > profit:
                        profit = highest - price
        return profit


