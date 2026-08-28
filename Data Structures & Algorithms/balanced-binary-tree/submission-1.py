# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(node):
            nonlocal isBalanced
            if not node: return 0
            left, right = 0, 0
            right = 1 + dfs(node.right)
            left = 1 + dfs(node.left)
            if abs(left - right) > 1: isBalanced = False
            return max(left, right)
        dfs(root)
        return isBalanced