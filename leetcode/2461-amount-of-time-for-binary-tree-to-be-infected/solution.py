from collections import deque, defaultdict
from typing import Optional

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    adj[node.val].append(child.val)
                    adj[child.val].append(node.val)
                    stack.append(child)

        seen = {start}
        q = deque([start])
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
        return minutes
