from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        entries = []

        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if not node:
                return
            entries.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        entries.sort()

        result = []
        prev_col = None
        for col, _, val in entries:
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].append(val)

        return result
