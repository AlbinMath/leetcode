class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        flat = sorted(v for row in values for v in row)
        return sum(v * d for d, v in enumerate(flat, 1))
