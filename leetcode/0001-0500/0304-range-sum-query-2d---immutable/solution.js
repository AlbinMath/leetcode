
var NumMatrix = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    this.prefix = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            this.prefix[r + 1][c + 1] =
                matrix[r][c] +
                this.prefix[r][c + 1] +
                this.prefix[r + 1][c] -
                this.prefix[r][c];
        }
    }
};

NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    return (
        this.prefix[row2 + 1][col2 + 1] -
        this.prefix[row1][col2 + 1] -
        this.prefix[row2 + 1][col1] +
        this.prefix[row1][col1]
    );
};
