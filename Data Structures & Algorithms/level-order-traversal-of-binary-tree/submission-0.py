# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = [(root, 0)]
        while queue:
            curr, depth = queue.pop(0)
            if not curr: continue
            if len(ans) == depth:
                ans.append([curr.val])
            else:
                ans[depth].append(curr.val)
            queue.append((curr.left, depth + 1))
            queue.append((curr.right, depth + 1))
        return ans