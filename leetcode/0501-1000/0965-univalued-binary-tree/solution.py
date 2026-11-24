
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val

        def dfs(node):
            if node is None:
                return True

            if node.val != value:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)

