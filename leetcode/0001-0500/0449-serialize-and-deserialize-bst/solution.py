# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        vals = []
        
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        vals = [int(x) for x in data.split()]
        idx = 0
        
        def build(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx >= len(vals):
                return None
            
            val = vals[idx]
            if not (lower < val < upper):
                return None
            
            idx += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node
            
        return build()
