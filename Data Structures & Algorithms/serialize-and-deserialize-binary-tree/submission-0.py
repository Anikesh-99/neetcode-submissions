# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
    
        def traverse(node):
            if not node: 
                result.append(str("N"))
                return
            result.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
            
        traverse(root)
        return "/".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split("/")
        lst = [int(item) if item != "N" else item for item in lst]
        # print(lst)
        idx = 0
        def buildTree():
            nonlocal idx
            if idx >= len(lst) or lst[idx] == "N": 
                idx += 1
                return None
            # print()
            node = TreeNode(lst[idx])
            idx += 1
            node.left = buildTree()
            node.right = buildTree()
            return node
        return buildTree() 
