var minFallingPathSum = function(grid) {
    const n = grid.length;
    // Track smallest sum (min1), its column index (min1Col), and second smallest sum (min2)
    let min1 = 0;
    let min2 = 0;
    let min1Col = -1;

    for (let r = 0; r < n; r++) {
        let nextMin1 = Infinity;
        let nextMin2 = Infinity;
        let nextMin1Col = -1;

        for (let c = 0; c < n; c++) {
            const prevBest = c === min1Col ? min2 : min1;
            const currSum = grid[r][c] + prevBest;

            if (currSum < nextMin1) {
                nextMin2 = nextMin1;
                nextMin1 = currSum;
                nextMin1Col = c;
            } else if (currSum < nextMin2) {
                nextMin2 = currSum;
            }
        }

        min1 = nextMin1;
        min2 = nextMin2;
        min1Col = nextMin1Col;
    }

    return min1;
};
