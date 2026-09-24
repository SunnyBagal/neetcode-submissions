class Solution:
    def maxProfit(self, prices: List[int]) -> int:

      minPrice = prices[0]
      maxi = 0

      for i in prices:
        if i < minPrice:
          minPrice = i

        profit = i - minPrice
        maxi = max(maxi, profit)

      return maxi
