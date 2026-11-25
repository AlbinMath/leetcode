class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])  # radius 0
                k = 1
                while i + 2 * k < m and j - k >= 0 and j + k < n:
                    s = 0
                    for t in range(k):
                        s += grid[i + t][j + t]
                        s += grid[i + k + t][j + k - t]
                        s += grid[i + 2 * k - t][j - t]
                        s += grid[i + k - t][j - k + t]
                    sums.add(s)
                    k += 1

        return sorted(sums, reverse=True)[:3]
