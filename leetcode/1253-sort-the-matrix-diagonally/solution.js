
var diagonalSort = function(mat) {
    const m = mat.length;
    const n = mat[0].length;

    const sortDiagonal = (startR, startC) => {
        const diag = [];
        let r = startR;
        let c = startC;
        while (r < m && c < n) {
            diag.push(mat[r][c]);
            r++;
            c++;
        }
        diag.sort((a, b) => a - b);
        r = startR;
        c = startC;
        for (const val of diag) {
            mat[r][c] = val;
            r++;
            c++;
        }
    };
    for (let c = 0; c < n; c++) {
        sortDiagonal(0, c);
    }
    for (let r = 1; r < m; r++) {
        sortDiagonal(r, 0);
    }

    return mat;
};
