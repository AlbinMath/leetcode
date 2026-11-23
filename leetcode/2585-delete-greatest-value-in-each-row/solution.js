var deleteGreatestValue = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // Sort each row in ascending order
    for (const row of grid) {
        row.sort((a, b) => a - b);
    }

    let answer = 0;
    // Sum the maximum value across all rows for each column
    for (let j = 0; j < n; j++) {
        let colMax = 0;
        for (let i = 0; i < m; i++) {
            colMax = Math.max(colMax, grid[i][j]);
        }
        answer += colMax;
    }

    return answer;
};
