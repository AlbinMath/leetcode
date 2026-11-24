from typing import Optional

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]

        while stack:
            node, mask = stack.pop()
            mask ^= 1 << node.val
            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    ans += 1
                continue
            if node.left:
                stack.append((node.left, mask))
            if node.right:
                stack.append((node.right, mask))

        return ans
