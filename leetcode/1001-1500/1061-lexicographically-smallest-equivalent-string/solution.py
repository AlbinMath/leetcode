class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                # Always attach the lexicographically larger root to the smaller one
                if rx < ry:
                    parent[ry] = rx
                else:
                    parent[rx] = ry

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        res = []
        for ch in baseStr:
            root_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            res.append(root_char)

        return "".join(res)
