class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        cand1 = None
        cand2 = None
        
        # Step 1: Check for any node with two parents
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u
            
        # Step 2: Union-Find initialization
        uf = list(range(n + 1))
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            uf[root_x] = root_y
            return True

        # Step 3: Process edges with Union-Find
        for u, v in edges:
            # Skip cand2 to test if removing it resolves the tree
            if [u, v] == cand2:
                continue
            
            # If adding [u, v] causes a cycle
            if not union(u, v):
                # If there was a double parent, cand1 is part of the cycle
                if cand1:
                    return cand1
                # Otherwise, this edge creates the cycle (Case 3)
                return [u, v]
                
        # If no cycle was detected, skipping cand2 was the correct fix
        return cand2
