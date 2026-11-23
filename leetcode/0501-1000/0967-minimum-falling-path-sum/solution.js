var minFallingPathSum = function(matrix) {
    const n = matrix.length;
    let dp = [...matrix[0]];

    for (let r = 1; r < n; r++) {
        const nextDp = new Array(n);
        for (let c = 0; c < n; c++) {
            let bestPrev = dp[c];
            if (c > 0 && dp[c - 1] < bestPrev) bestPrev = dp[c - 1];
            if (c + 1 < n && dp[c + 1] < bestPrev) bestPrev = dp[c + 1];
            nextDp[c] = matrix[r][c] + bestPrev;
        }
        dp = nextDp;
    }

    return Math.min(...dp);
};
