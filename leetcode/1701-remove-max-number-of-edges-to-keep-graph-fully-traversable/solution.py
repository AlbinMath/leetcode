class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.components -= 1
            return True
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_dsu = DSU(n)
        bob_dsu = DSU(n)
        edges_used = 0

        # Step 1: Greedily add Type 3 edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                a_used = alice_dsu.union(u, v)
                b_used = bob_dsu.union(u, v)
                if a_used or b_used:
                    edges_used += 1

        # Step 2: Add Type 1 (Alice) and Type 2 (Bob) edges
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice_dsu.union(u, v):
                    edges_used += 1
            elif edge_type == 2:
                if bob_dsu.union(u, v):
                    edges_used += 1

        # Step 3: Check if both graphs are fully connected
        if alice_dsu.components == 1 and bob_dsu.components == 1:
            return len(edges) - edges_used

        return -1
