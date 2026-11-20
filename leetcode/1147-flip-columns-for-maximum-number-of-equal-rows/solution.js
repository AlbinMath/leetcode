var maxEqualRowsAfterFlips = function(matrix) {
    const patternCounts = new Map();
    let maxRows = 0;

    for (const row of matrix) {
        // Normalize row so its first bit is always 0 (XOR all bits with row[0])
        const first = row[0];
        let pattern = '';
        for (let c = 0; c < row.length; c++) {
            pattern += (row[c] ^ first);
        }

        const count = (patternCounts.get(pattern) || 0) + 1;
        patternCounts.set(pattern, count);
        if (count > maxRows) {
            maxRows = count;
        }
    }

    return maxRows;
};
