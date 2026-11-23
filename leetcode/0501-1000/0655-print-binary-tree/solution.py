from typing import List, Optional

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
            
        height = get_height(root)
        m = height + 1
        n = (1 << (height + 1)) - 1
        res = [[""] * n for _ in range(m)]
        
        def fill(node: Optional[TreeNode], r: int, c: int) -> None:
            if not node:
                return
            res[r][c] = str(node.val)
            if r < height:
                offset = 1 << (height - r - 1)
                if node.left:
                    fill(node.left, r + 1, c - offset)
                if node.right:
                    fill(node.right, r + 1, c + offset)
                    
        fill(root, 0, (n - 1) >> 1)
        return res
