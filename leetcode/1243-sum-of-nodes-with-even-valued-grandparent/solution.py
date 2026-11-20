from typing import Optional

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grand):
            if not node:
                return 0
            total = node.val if grand % 2 == 0 else 0
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total

        return dfs(root, 1, 1)
