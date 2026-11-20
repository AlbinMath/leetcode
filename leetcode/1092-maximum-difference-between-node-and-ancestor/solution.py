from typing import Optional

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, root.val, root.val)]  # (node, path min, path max)
        while stack:
            node, lo, hi = stack.pop()
            lo = min(lo, node.val)
            hi = max(hi, node.val)
            ans = max(ans, hi - lo)
            if node.left:
                stack.append((node.left, lo, hi))
            if node.right:
                stack.append((node.right, lo, hi))
        return ans
