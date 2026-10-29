class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        
        def build(bound=float('inf')) -> Optional[TreeNode]:
            nonlocal idx
            if idx == len(preorder) or preorder[idx] > bound:
                return None
            
            val = preorder[idx]
            idx += 1
            node = TreeNode(val)
            
            node.left = build(val)
            node.right = build(bound)
            
            return node
            
        return build()
