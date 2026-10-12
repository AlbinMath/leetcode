var equalPairs = function(grid) {
    const n = grid.length;
    const rowMap = new Map();
    let count = 0;

    // Store each row and its frequency
    for (let i = 0; i < n; i++) {
        const key = grid[i].join(",");
        rowMap.set(key, (rowMap.get(key) || 0) + 1);
    }

    // Build each column and check matching rows
    for (let j = 0; j < n; j++) {
        const column = [];

        for (let i = 0; i < n; i++) {
            column.push(grid[i][j]);
        }

        const key = column.join(",");
        count += rowMap.get(key) || 0;
    }

    return count;
};
