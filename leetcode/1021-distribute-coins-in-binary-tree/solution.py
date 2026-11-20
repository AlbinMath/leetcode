from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            moves += abs(l) + abs(r)
            return node.val + l + r - 1

        dfs(root)
        return moves
