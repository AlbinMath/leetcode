from collections import deque
from typing import Optional

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        level = [root]
        while level:
            # sum of original values on the next level
            next_sum = 0
            for node in level:
                if node.left:
                    next_sum += node.left.val
                if node.right:
                    next_sum += node.right.val

            nxt = []
            for node in level:
                sib = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = next_sum - sib
                    nxt.append(node.left)
                if node.right:
                    node.right.val = next_sum - sib
                    nxt.append(node.right)
            level = nxt
        return root
