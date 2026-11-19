from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                blacks = sum(grid[r + dr][c + dc] == 'B'
                             for dr in (0, 1) for dc in (0, 1))
                if blacks != 2:
                    return True
        return False
