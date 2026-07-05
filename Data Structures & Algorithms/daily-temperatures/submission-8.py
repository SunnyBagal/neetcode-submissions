class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

      res = [0] * len(temperatures)
      stack = []
      n = len(temperatures)
      nums = temperatures

      for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
          prev = stack.pop()
          res[prev] = i - prev
        stack.append(i)

      return res
