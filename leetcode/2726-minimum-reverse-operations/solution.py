from collections import deque
from typing import List

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned_set = set(banned)
        ans = [-1] * n
        ans[p] = 0

        # Maintain two DSUs: one for even indices, one for odd indices
        # parent[i] points to the next available unvisited index of the same parity
        parent = list(range(n + 2))

        def find(x: int) -> int:
            path = []
            while parent[x] != x:
                path.append(x)
                x = parent[x]
            for node in path:
                parent[node] = x
            return x

        def remove(x: int):
            # Point to next node of the same parity
            parent[x] = find(x + 2)

        # Remove banned nodes and the start node p from the DSU
        for b in banned:
            remove(b)
        remove(p)

        queue = deque([p])

        while queue:
            curr = queue.popleft()
            d = ans[curr]

            # Calculate the range [min_pos, max_pos]
            min_pos = max(curr - k + 1, k - 1 - curr)
            max_pos = min(curr + k - 1, 2 * n - k - 1 - curr)

            # Find unvisited nodes in range with same parity as (curr + k - 1)
            nxt = find(min_pos)
            while nxt <= max_pos:
                ans[nxt] = d + 1
                queue.append(nxt)
                remove(nxt)
                nxt = find(nxt)

        return ans
