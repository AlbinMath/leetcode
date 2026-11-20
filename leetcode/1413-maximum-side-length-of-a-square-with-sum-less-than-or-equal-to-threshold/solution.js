var maxSideLength = function(mat, threshold) {
    const m = mat.length;
    const n = mat[0].length;
    const prefix = Array.from({ length: m + 1 }, () => new Int32Array(n + 1));

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            prefix[r + 1][c + 1] =
                mat[r][c] +
                prefix[r][c + 1] +
                prefix[r + 1][c] -
                prefix[r][c];
        }
    }

    const squareSum = (r2, c2, side) => {
        const r1 = r2 - side;
        const c1 = c2 - side;
        return prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
    };

    let maxLen = 0;
    for (let r = 1; r <= m; r++) {
        for (let c = 1; c <= n; c++) {
            // Only test side length = maxLen + 1 to see if we can improve our best answer
            const candidate = maxLen + 1;
            if (r >= candidate && c >= candidate && squareSum(r, c, candidate) <= threshold) {
                maxLen = candidate;
            }
        }
    }

    return maxLen;
};
