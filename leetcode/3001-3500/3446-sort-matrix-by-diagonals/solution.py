class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = {}

        for i in range(n):
            for j in range(n):
                diags.setdefault(i - j, []).append(grid[i][j])

        for d, vals in diags.items():
            vals.sort(reverse=(d >= 0))
        idx = {d: 0 for d in diags}
        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diags[d][idx[d]]
                idx[d] += 1

        return grid
