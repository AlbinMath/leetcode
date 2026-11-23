var maxIncreaseKeepingSkyline = function(grid) {
    const n = grid.length;
    const rowMax = new Array(n).fill(0);
    const colMax = new Array(n).fill(0);

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const val = grid[r][c];
            if (val > rowMax[r]) rowMax[r] = val;
            if (val > colMax[c]) colMax[c] = val;
        }
    }

    let totalIncrease = 0;
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            totalIncrease += Math.min(rowMax[r], colMax[c]) - grid[r][c];
        }
    }

    return totalIncrease;
};
