from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        
        for row in wall:
            prefix_width = 0
            for brick in row[:-1]:
                prefix_width += brick
                edge_counts[prefix_width] += 1
                
        max_aligned_edges = max(edge_counts.values(), default=0)
        return len(wall) - max_aligned_edges
