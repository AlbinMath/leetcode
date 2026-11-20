from collections import deque
from typing import Optional

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(vals):
            k = len(vals)
            order = sorted(range(k), key=lambda i: vals[i])
            # order[j] = index of the element that belongs at position j
            seen = [False] * k
            swaps = 0
            for i in range(k):
                if seen[i] or order[i] == i:
                    continue
                length = 0
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = order[j]
                    length += 1
                swaps += length - 1
            return swaps

        ans = 0
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += min_swaps(vals)
        return ans
