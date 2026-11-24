from collections import deque
from typing import Optional
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = 0 if level % 2 == 0 else float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                v = node.val
                if level % 2 == 0:
                    if v % 2 == 0 or v <= prev:
                        return False
                else:
                    if v % 2 == 1 or v >= prev:
                        return False
                prev = v
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
