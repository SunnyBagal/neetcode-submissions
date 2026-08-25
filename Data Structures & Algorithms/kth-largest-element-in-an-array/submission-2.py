class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        point = heapq.nlargest(k, nums)

        return (point[k - 1])
