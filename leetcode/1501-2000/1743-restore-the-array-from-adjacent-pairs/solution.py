from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        # Find either endpoint (degree == 1)
        start = next(node for node, neighbors in graph.items() if len(neighbors) == 1)
        
        n = len(adjacentPairs) + 1
        nums = [start, graph[start][0]]
        
        # Walk along the chain without needing a visited set by avoiding the previous node
        while len(nums) < n:
            prev, curr = nums[-2], nums[-1]
            a, b = graph[curr]
            nums.append(b if a == prev else a)
            
        return nums
