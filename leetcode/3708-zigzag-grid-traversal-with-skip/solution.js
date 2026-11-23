var zigzagTraversal = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const result = [];
    let take = true;

    for (let r = 0; r < rows; r++) {
        if (r % 2 === 0) {
            for (let c = 0; c < cols; c++) {
                if (take) result.push(grid[r][c]);
                take = !take;
            }
        } else {
            for (let c = cols - 1; c >= 0; c--) {
                if (take) result.push(grid[r][c]);
                take = !take;
            }
        }
    }

    return result;
};
