class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m
        res = [[0] * m for _ in range(n)]

        # prefix pass: res holds the product of everything before the cell
        pre = 1
        for k in range(total):
            i, j = divmod(k, m)
            res[i][j] = pre
            pre = pre * grid[i][j] % MOD

        # suffix pass: multiply by the product of everything after the cell
        suf = 1
        for k in range(total - 1, -1, -1):
            i, j = divmod(k, m)
            res[i][j] = res[i][j] * suf % MOD
            suf = suf * grid[i][j] % MOD

        return res
