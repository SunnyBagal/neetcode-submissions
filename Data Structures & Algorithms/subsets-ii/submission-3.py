class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        def func(index, subset):
            if index == len(nums):
                res.add(tuple(subset))
                return 

            subset.append(nums[index])
            func(index + 1, subset)
            subset.pop()
            func(index + 1, subset)

        nums.sort()
        func(0, [])

        return [list(s) for s in res]