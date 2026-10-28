/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPaths = function (grid) {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const total = m * n;

    const order = new Array(total);
    for (let i = 0; i < total; i++) order[i] = i;
    order.sort((a, b) => grid[(b / n) | 0][b % n] - grid[(a / n) | 0][a % n]); // descending

    const dp = new Int32Array(total);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let ans = 0;

    for (const c of order) {
        const i = (c / n) | 0, j = c % n;
        let cnt = 1;
        for (const [di, dj] of dirs) {
            const ni = i + di, nj = j + dj;
            if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
            if (grid[ni][nj] > grid[i][j]) cnt = (cnt + dp[ni * n + nj]) % MOD;
        }
        dp[c] = cnt;
        ans = (ans + cnt) % MOD;
    }
    return ans;
};
