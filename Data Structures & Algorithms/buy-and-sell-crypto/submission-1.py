class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]      # 10
        maxPrice = float("-inf")  # -inf

        for sell in prices:
          if sell < minPrice :
            minPrice = sell

          profit = sell - minPrice

          maxPrice = max(maxPrice, profit)
        
        return maxPrice
