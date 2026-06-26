# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def helper(root):
            nonlocal mx
            if not root: return 0
            l = helper(root.left)
            r = helper(root.right)
            mx = max(mx, l + r)
            return 1 + max(l, r)
        helper(root)
        return mx