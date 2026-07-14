class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]      # 10
        maxPrice = float("-inf")  # -inf

        for i in prices:
          if i < minPrice :
            minPrice = i
            
          profit = i - minPrice

          maxPrice = max(maxPrice, profit)
        
        return maxPrice
