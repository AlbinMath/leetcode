
var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // Initialize the first column.
    for (let i = 1; i < m; i++) {
        grid[i][0] += grid[i - 1][0];
    }

    // Initialize the first row.
    for (let j = 1; j < n; j++) {
        grid[0][j] += grid[0][j - 1];
    }

    // Calculate the minimum sum for each remaining cell.
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            grid[i][j] += Math.min(
                grid[i - 1][j],  // From above
                grid[i][j - 1]   // From the left
            );
        }
    }

    return grid[m - 1][n - 1];
};

