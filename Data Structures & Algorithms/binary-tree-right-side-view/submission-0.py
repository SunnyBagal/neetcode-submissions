# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

      if root is None:
        return []

      que = deque([root])
      res = []

      while que:
        level_size = len(que)

        for i in range(level_size):
          e = que.popleft()

          if i == level_size - 1:
              res.append(e.val)

          if e.left is not None:
              que.append(e.left)
          if e.right is not None:
              que.append(e.right)

      return res