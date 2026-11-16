from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, remaining):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right:
                if remaining == 0:
                    res.append(path[:])  # copy, since path keeps changing
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()  # backtrack

        dfs(root, targetSum)
        return res
