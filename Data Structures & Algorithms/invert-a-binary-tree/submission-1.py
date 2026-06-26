# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right): return root
        # print(root.val, root.left.val, root.right)
        l, r = root.left, root.right
        if not l:
            root.left = self.invertTree(r)
            root.right = None
        elif not r:
            root.right = self.invertTree(l)
            root.left = None
        else:
            root.left = self.invertTree(r)
            root.right = self.invertTree(l)
        return root