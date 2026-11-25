class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = [v for row in grid for v in row]
        r = vals[0] % x
        for v in vals:
            if v % x != r:
                return -1

        vals.sort()
        med = vals[len(vals) // 2]
        return sum(abs(v - med) // x for v in vals)
