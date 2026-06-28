# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if not curr: continue
            if p.val <= curr.val and q.val >= curr.val: return curr
            if p.val > curr.val:
                queue.append(curr.right)
            elif q.val < curr.val:
                queue.append(curr.left)
        return None


