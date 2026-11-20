from typing import List, Optional

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        i = 0

        def dfs(node) -> bool:
            nonlocal i
            if not node:
                return True
            if node.val != voyage[i]:
                return False
            i += 1
            if node.left and i < len(voyage) and node.left.val != voyage[i]:
                flipped.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)

        return flipped if dfs(root) else [-1]
