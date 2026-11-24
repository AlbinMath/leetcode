from typing import Optional



class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = None

        def dfs(node, suffix: str) -> None:
            nonlocal best
            if not node:
                return
            cur = chr(node.val + 97) + suffix  # prepend: path now reads node -> root
            if not node.left and not node.right:
                if best is None or cur < best:
                    best = cur
                return
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, "")
        return best
