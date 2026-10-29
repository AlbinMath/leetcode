from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        if cnt0 == 0:
            return 0

        # parent[i] points to the next unvisited integer of the same parity >= i
        parent = list(range(n + 3))

        def find(x: int) -> int:
            path = []
            while parent[x] != x:
                path.append(x)
                x = parent[x]
            for node in path:
                parent[node] = x
            return x

        def remove(x: int):
            parent[x] = find(x + 2)

        # Remove the initial state
        remove(cnt0)

        queue = deque([(cnt0, 0)])

        while queue:
            cur, dist = queue.popleft()

            # Bound x (the number of 0s flipped to 1s)
            x_min = max(0, k - n + cur)
            x_max = min(cur, k)

            l = cur + k - 2 * x_max
            r = cur + k - 2 * x_min

            # Search in the range [l, r] with parity matching (cur + k) % 2
            nxt = find(l)
            while nxt <= r:
                if nxt == 0:
                    return dist + 1
                queue.append((nxt, dist + 1))
                remove(nxt)
                nxt = find(nxt)

        return -1
