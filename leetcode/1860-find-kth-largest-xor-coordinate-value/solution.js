/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthLargestValue = function(matrix, k) {
    const m = matrix.length;
    const n = matrix[0].length;
    const values = [];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) matrix[i][j] ^= matrix[i - 1][j];
            if (j > 0) matrix[i][j] ^= matrix[i][j - 1];
            if (i > 0 && j > 0) matrix[i][j] ^= matrix[i - 1][j - 1];

            values.push(matrix[i][j]);
        }
    }

    values.sort((a, b) => b - a);
    return values[k - 1];
};
