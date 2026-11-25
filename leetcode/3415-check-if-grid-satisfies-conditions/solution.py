class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        first = grid[0]
        if any(first[j] == first[j + 1] for j in range(len(first) - 1)):
            return False
        return all(row == first for row in grid)
