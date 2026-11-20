
var cherryPickup = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let dp = Array.from({ length: cols }, () => new Int32Array(cols));

    for (let r = rows - 1; r >= 0; r--) {
        const nextDp = Array.from({ length: cols }, () => new Int32Array(cols));
        for (let c1 = 0; c1 < cols; c1++) {
            for (let c2 = 0; c2 < cols; c2++) {
                const cherries = grid[r][c1] + (c1 === c2 ? 0 : grid[r][c2]);
                let bestNext = 0;

                if (r < rows - 1) {
                    for (let d1 = -1; d1 <= 1; d1++) {
                        const nc1 = c1 + d1;
                        if (nc1 < 0 || nc1 >= cols) continue;
                        for (let d2 = -1; d2 <= 1; d2++) {
                            const nc2 = c2 + d2;
                            if (nc2 < 0 || nc2 >= cols) continue;
                            if (dp[nc1][nc2] > bestNext) {
                                bestNext = dp[nc1][nc2];
                            }
                        }
                    }
                }

                nextDp[c1][c2] = cherries + bestNext;
            }
        }
        dp = nextDp;
    }

    return dp[0][cols - 1];
};
