# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

      if root is None:
        return []

      queue = deque([root])
      res = []

      while len(queue) != 0:
        currentRes = []

        for i in range(len(queue)):
          currentRes.append(queue[i].val)

        res.append(currentRes)

        for i in range(len(queue)):
          current = queue.popleft()

          if current.left is not None:
            queue.append(current.left)

          if current.right is not None:
            queue.append(current.right)

      return res