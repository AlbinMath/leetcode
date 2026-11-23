var countUnguarded = function(m, n, guards, walls) {
    // 0 = unguarded, 1 = guard, 2 = wall, 3 = guarded
    const grid = Array.from({ length: m }, () => new Uint8Array(n));
    
    for (const [r, c] of guards) grid[r][c] = 1;
    for (const [r, c] of walls) grid[r][c] = 2;
    
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    
    for (const [r, c] of guards) {
        for (const [dr, dc] of directions) {
            let nr = r + dr;
            let nc = c + dc;
            while (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                if (grid[nr][nc] === 1 || grid[nr][nc] === 2) {
                    break;
                }
                grid[nr][nc] = 3;
                nr += dr;
                nc += dc;
            }
        }
    }
    
    let unguarded = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 0) unguarded++;
        }
    }
    
    return unguarded;
};
