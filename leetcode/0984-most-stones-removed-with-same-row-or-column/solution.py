class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x: int) -> int:
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for x, y in stones:
            # Distinguish row x from column y by using bitwise NOT (~y = -y - 1)
            union(x, ~y)

        # Count the number of distinct components
        unique_roots = {find(x) for x in parent}
        
        return len(stones) - len(unique_roots)
