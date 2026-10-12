var nearestExit = function(maze, entrance) {
    const m = maze.length;
    const n = maze[0].length;

    const queue = [[entrance[0], entrance[1], 0]];
    let front = 0;

    // Mark entrance as visited
    maze[entrance[0]][entrance[1]] = '+';

    const directions = [
        [-1, 0], // Up
        [1, 0],  // Down
        [0, -1], // Left
        [0, 1]   // Right
    ];

    while (front < queue.length) {
        const [row, col, steps] = queue[front++];

        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;

            // Check boundaries
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                continue;
            }

            // Skip walls and visited cells
            if (maze[nr][nc] === '+') {
                continue;
            }

            // Check whether this cell is an exit
            if (
                nr === 0 ||
                nr === m - 1 ||
                nc === 0 ||
                nc === n - 1
            ) {
                return steps + 1;
            }

            // Mark as visited and add to queue
            maze[nr][nc] = '+';
            queue.push([nr, nc, steps + 1]);
        }
    }

    return -1;
};
