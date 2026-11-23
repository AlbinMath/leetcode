var reconstructMatrix = function(upper, lower, colsum) {
    const n = colsum.length;
    let totalSum = 0;
    for (let i = 0; i < n; i++) {
        totalSum += colsum[i];
    }
    if (upper + lower !== totalSum) {
        return [];
    }

    const row0 = new Array(n).fill(0);
    const row1 = new Array(n).fill(0);

    // Pass 1: Place mandatory 1s for columns with colsum[i] === 2
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 2) {
            if (upper === 0 || lower === 0) {
                return [];
            }
            row0[i] = 1;
            row1[i] = 1;
            upper--;
            lower--;
        }
    }

    // Pass 2: Distribute remaining upper and lower budgets across colsum[i] === 1
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 1) {
            if (upper > 0) {
                row0[i] = 1;
                upper--;
            } else {
                row1[i] = 1;
                lower--;
            }
        }
    }

    return [row0, row1];
};
