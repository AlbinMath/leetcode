class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        running_sum = 0
        
        def traverse(node: TreeNode):
            nonlocal running_sum
            if not node:
                return
            
            # 1. Visit larger nodes
            traverse(node.right)
            
            # 2. Update current node
            running_sum += node.val
            node.val = running_sum
            
            # 3. Visit smaller nodes
            traverse(node.left)
            
        traverse(root)
        return root
