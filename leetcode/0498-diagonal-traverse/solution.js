/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const res = new Array(m * n);
    let r = 0;
    let c = 0;
    let upRight = true;

    for (let i = 0; i < m * n; i++) {
        res[i] = mat[r][c];

        if (upRight) {
            if (c === n - 1) {
                r++;
                upRight = false;
            } else if (r === 0) {
                c++;
                upRight = false;
            } else {
                r--;
                c++;
            }
        } else {
            if (r === m - 1) {
                c++;
                upRight = true;
            } else if (c === 0) {
                r++;
                upRight = true;
            } else {
                r++;
                c--;
            }
        }
    }

    return res;
};
