class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = 0
        bestbuy = prices[0]

        for price in prices:
            if price > bestbuy:
                maxprofit = max(maxprofit, price - bestbuy)
            bestbuy = min(bestbuy, price)
        return maxprofit