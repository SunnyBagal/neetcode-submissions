class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        sol = []
        ans = []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return 

            for value in nums:
                if value not in sol:
                    sol.append(value)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return ans

        # Time Complexity : O(n!)
        # Space Complexity : O(n)
