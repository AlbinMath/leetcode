
var numMagicSquaresInside = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    if (rows < 3 || cols < 3) return 0;

    const isMagic = (r, c) => {
        // In any 3x3 magic square using 1..9, the center element must be 5
        if (grid[r + 1][c + 1] !== 5) return false;

        // Check all 9 cells are distinct values in [1, 9] using a bitmask
        let mask = 0;
        for (let i = r; i < r + 3; i++) {
            for (let j = c; j < c + 3; j++) {
                const val = grid[i][j];
                if (val < 1 || val > 9 || (mask & (1 << val)) !== 0) {
                    return false;
                }
                mask |= (1 << val);
            }
        }

        // Check rows, columns, and both diagonals sum to 15
        for (let i = 0; i < 3; i++) {
            if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] !== 15) return false;
            if (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] !== 15) return false;
        }

        return (
            grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] === 15 &&
            grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] === 15
        );
    };

    let count = 0;
    for (let r = 0; r <= rows - 3; r++) {
        for (let c = 0; c <= cols - 3; c++) {
            if (isMagic(r, c)) count++;
        }
    }

    return count;
};
