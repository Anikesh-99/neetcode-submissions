# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if not node: return 0
            leftMx = max(0, dfs(node.left))
            rightMx = max(0, dfs(node.right))
            res = max(res, node.val + leftMx + rightMx)
            return node.val + max(leftMx, rightMx)
        dfs(root)
        return res