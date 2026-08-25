class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        data = nums
        point = heapq.nlargest(k, data)

        return (point[k - 1])
