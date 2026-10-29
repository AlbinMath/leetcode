class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Collect values in sorted order via in-order traversal
        sorted_vals = []
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Build a balanced BST from the sorted array
        def build_balanced(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(sorted_vals[mid])
            root.left = build_balanced(left, mid - 1)
            root.right = build_balanced(mid + 1, right)
            
            return root
            
        return build_balanced(0, len(sorted_vals) - 1)
