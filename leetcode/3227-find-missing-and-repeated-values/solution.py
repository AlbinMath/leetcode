class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for row in grid:
            for v in row:
                cnt[v] += 1

        a = b = 0
        for x in range(1, n * n + 1):
            if cnt[x] == 2:
                a = x
            elif cnt[x] == 0:
                b = x
        return [a, b]
