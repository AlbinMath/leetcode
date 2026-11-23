/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    let startRow = 0;
    let startCol = 0;
    let emptyCount = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                startRow = i;
                startCol = j;
            }

            if (grid[i][j] !== -1) {
                emptyCount++;
            }
        }
    }

    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    function dfs(row, col, remaining) {
        if (grid[row][col] === 2) {
            return remaining === 1 ? 1 : 0;
        }

        const original = grid[row][col];
        grid[row][col] = -1;

        let paths = 0;

        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;

            if (
                nr >= 0 && nr < m &&
                nc >= 0 && nc < n &&
                grid[nr][nc] !== -1
            ) {
                paths += dfs(nr, nc, remaining - 1);
            }
        }

        grid[row][col] = original;
        return paths;
    }

    return dfs(startRow, startCol, emptyCount);
};
