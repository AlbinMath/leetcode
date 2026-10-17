class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        return (sum(v > 0 for row in grid for v in row)
                + sum(map(max, grid))
                + sum(max(col) for col in zip(*grid)))
