var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    const totalCells = rows * cols;
    const res = [[rStart, cStart]];
    if (totalCells === 1) return res;

    // Clockwise directions: East, South, West, North
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let r = rStart;
    let c = cStart;
    let stepLen = 1;
    let d = 0; // Start facing East

    while (res.length < totalCells) {
        // Every two direction changes share the same step length
        for (let turn = 0; turn < 2; turn++) {
            const [dr, dc] = dirs[d];
            for (let s = 0; s < stepLen; s++) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    res.push([r, c]);
                    if (res.length === totalCells) return res;
                }
            }
            d = (d + 1) % 4;
        }
        stepLen++;
    }

    return res;
};
