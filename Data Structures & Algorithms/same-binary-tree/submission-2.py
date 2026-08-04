from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

      queue = deque([(p, q)])

      while queue:
        left, right = queue.popleft()
        

        if left is None and right is None:
          continue

        if left is None or right is None:
          return False

        if left.val != right.val:
          return False

        queue.append((left.left, right.left))
        queue.append((left.right, right.right))

      
      return True
