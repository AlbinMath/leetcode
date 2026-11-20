from collections import deque
from typing import Optional

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        q = deque([root])
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(total)

        if len(sums) < k:
            return -1
        sums.sort(reverse=True)
        return sums[k - 1]
