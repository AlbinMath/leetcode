
var numSpecial = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const rowSum = new Int32Array(m);
    const colSum = new Int32Array(n);

    // Pass 1: Count 1s in each row and column
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowSum[i]++;
                colSum[j]++;
            }
        }
    }

    // Pass 2: Count cells where mat[i][j] === 1 is the sole 1 in its row and column
    let special = 0;
    for (let i = 0; i < m; i++) {
        if (rowSum[i] === 1) {
            for (let j = 0; j < n; j++) {
                if (mat[i][j] === 1 && colSum[j] === 1) {
                    special++;
                    break;
                }
            }
        }
    }

    return special;
};
