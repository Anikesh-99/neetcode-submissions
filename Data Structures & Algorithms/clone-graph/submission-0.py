"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        hm = {}
        def helper(node):
            if node.val in hm: return hm[node.val]
            # print(node.val)
            hm[node.val] = Node(node.val, [])
            for n in node.neighbors:
                if n.val in hm:
                    hm[node.val].neighbors.append(hm[n.val])
                else:
                    hm[node.val].neighbors.append(helper(n))
            return hm[node.val]
        return helper(node) 