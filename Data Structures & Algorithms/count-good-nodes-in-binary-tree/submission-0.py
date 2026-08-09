# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      
      res = []

      def dfs(node, prev):
        if node is None:
          return 

        if node.val >= prev:
          res.append(node.val)

        prev = max(prev, node.val)

        dfs(node.left, prev)
        dfs(node.right, prev)

      dfs(root, float('-inf'))

      return len(res)