class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted((w, u, v, i) for i, (u, v, w) in enumerate(edges))

        def mst(skip=-1, pick=-1):
            p = list(range(n))

            def find(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            cost, cnt = 0, 0

            if pick != -1:
                w, u, v, _ = edges[pick]
                p[find(u)] = find(v)
                cost, cnt = w, 1

            for i, (w, u, v, _) in enumerate(edges):
                if i == skip:
                    continue
                a, b = find(u), find(v)
                if a != b:
                    p[a] = b
                    cost += w
                    cnt += 1

            return cost if cnt == n - 1 else float('inf')

        base = mst()
        critical, pseudo = [], []

        for i, edge in enumerate(edges):
            if mst(skip=i) > base:
                critical.append(edge[3])
            elif mst(pick=i) == base:
                pseudo.append(edge[3])

        return [critical, pseudo]
