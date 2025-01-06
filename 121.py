class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = float('inf')
        sell = 0
        for price in prices:
            
            min_price = min(min_price, price)

            profit = price - min_price

            sell = max(sell, profit)
            
            
        return sell

        
