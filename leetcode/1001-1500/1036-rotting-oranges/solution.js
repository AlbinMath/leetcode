
var orangesRotting = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const queue = [];
    let fresh = 0;
    let minutes = 0;
    let head = 0;

    // Find all rotten oranges and count fresh oranges
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 2) {
                queue.push([r, c]);
            } else if (grid[r][c] === 1) {
                fresh++;
            }
        }
    }

    const directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    // Process one BFS level per minute
    while (head < queue.length && fresh > 0) {
        const levelSize = queue.length - head;

        for (let i = 0; i < levelSize; i++) {
            const [r, c] = queue[head++];

            for (const [dr, dc] of directions) {
                const nr = r + dr;
                const nc = c + dc;

                if (
                    nr >= 0 && nr < m &&
                    nc >= 0 && nc < n &&
                    grid[nr][nc] === 1
                ) {
                    grid[nr][nc] = 2;
                    fresh--;
                    queue.push([nr, nc]);
                }
            }
        }

        minutes++;
    }

    return fresh === 0 ? minutes : -1;
};

