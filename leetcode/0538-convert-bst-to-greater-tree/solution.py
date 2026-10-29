class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        
        def reverse_inorder(node: Optional[TreeNode]):
            nonlocal running_sum
            if not node:
                return
            
            # 1. Visit all greater nodes first
            reverse_inorder(node.right)
            
            # 2. Update current node
            running_sum += node.val
            node.val = running_sum
            
            # 3. Visit smaller nodes
            reverse_inorder(node.left)
            
        reverse_inorder(root)
        return root
