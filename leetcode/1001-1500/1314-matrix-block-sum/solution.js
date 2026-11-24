
var matrixBlockSum = function(mat, k) {
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

    const answer = Array.from({ length: m }, () => new Array(n));
    for (let i = 0; i < m; i++) {
        const r1 = Math.max(0, i - k);
        const r2 = Math.min(m - 1, i + k);
        for (let j = 0; j < n; j++) {
            const c1 = Math.max(0, j - k);
            const c2 = Math.min(n - 1, j + k);
            answer[i][j] =
                prefix[r2 + 1][c2 + 1] -
                prefix[r1][c2 + 1] -
                prefix[r2 + 1][c1] +
                prefix[r1][c1];
        }
    }

    return answer;
};
