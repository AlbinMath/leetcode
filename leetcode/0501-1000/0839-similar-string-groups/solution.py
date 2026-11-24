class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            nonlocal components
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                components -= 1
                return True
            return False

        def is_similar(s1: str, s2: str) -> bool:
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    union(i, j)

        return components
