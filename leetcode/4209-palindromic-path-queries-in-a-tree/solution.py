
class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Build parent, depth, and traversal order iteratively.
        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]
        parent[0] = 0

        while stack:
            u = stack.pop()
            order.append(u)

            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        # 2. Calculate subtree sizes and heavy children.
        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # 3. Heavy-Light Decomposition.
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            start, chain_head = stack.pop()
            u = start

            while u != -1:
                head[u] = chain_head
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # 4. Segment tree: XOR of character parity masks.
        base = 1
        while base < n:
            base <<= 1

        seg = [0] * (2 * base)
        chars = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            seg[base + pos[u]] = chars[u]

        for i in range(base - 1, 0, -1):
            seg[i] = seg[i << 1] ^ seg[i << 1 | 1]

        def point_update(p, value):
            p += base
            seg[p] = value
            p >>= 1

            while p:
                seg[p] = seg[p << 1] ^ seg[p << 1 | 1]
                p >>= 1

        def range_query(left, right):
            # Inclusive range [left, right].
            left += base
            right += base
            result = 0

            while left <= right:
                if left & 1:
                    result ^= seg[left]
                    left += 1

                if not (right & 1):
                    result ^= seg[right]
                    right -= 1

                left >>= 1
                right >>= 1

            return result

        # 5. XOR all character masks along a tree path.
        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_query(pos[u], pos[v])
            return result

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))

                if chars[u] != new_mask:
                    chars[u] = new_mask
                    point_update(pos[u], new_mask)

            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_query(u, v)

                # At most one character may have odd frequency.
                ans.append((mask & (mask - 1)) == 0)

        return ans

