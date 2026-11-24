var countSquares = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const dp = new Int32Array(n);
    let totalSquares = 0;

    for (let r = 0; r < m; r++) {
        let prevDiag = 0; // Stores dp[r - 1][c - 1]
        for (let c = 0; c < n; c++) {
            const temp = dp[c]; // Save dp[r - 1][c] before overwriting
            if (matrix[r][c] === 1) {
                if (r === 0 || c === 0) {
                    dp[c] = 1;
                } else {
                    dp[c] = 1 + Math.min(dp[c], dp[c - 1], prevDiag);
                }
                totalSquares += dp[c];
            } else {
                dp[c] = 0;
            }
            prevDiag = temp;
        }
    }

    return totalSquares;
};
