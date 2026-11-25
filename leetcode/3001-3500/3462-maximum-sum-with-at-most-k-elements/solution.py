class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        cand = []
        for row, lim in zip(grid, limits):
            if lim:
                cand.extend(sorted(row, reverse=True)[:lim])
        cand.sort(reverse=True)
        return sum(cand[:k])
