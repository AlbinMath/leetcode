
var largest1BorderedSquare = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    // Consecutive 1s ending at (r, c) horizontally (left) and vertically (up)
    const left = Array.from({ length: rows }, () => new Int32Array(cols));
    const up = Array.from({ length: rows }, () => new Int32Array(cols));

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === 1) {
                left[r][c] = (c > 0 ? left[r][c - 1] : 0) + 1;
                up[r][c] = (r > 0 ? up[r - 1][c] : 0) + 1;
            }
        }
    }

    let maxLen = 0;
    for (let r = rows - 1; r >= 0; r--) {
        for (let c = cols - 1; c >= 0; c--) {
            // Bottom and right edges already have at least `side` 1s
            let side = Math.min(left[r][c], up[r][c]);
            while (side > maxLen) {
                // Verify top edge and left edge also have at least `side` 1s
                if (left[r - side + 1][c] >= side && up[r][c - side + 1] >= side) {
                    maxLen = side;
                    break;
                }
                side--;
            }
        }
    }

    return maxLen * maxLen;
};
