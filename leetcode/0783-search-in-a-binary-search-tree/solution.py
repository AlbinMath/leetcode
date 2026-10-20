class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            root = root.left if val < root.val else root.right
        return None
