
var cherryPickup = function(grid) {
    const n = grid.length;
    const NEG_INF = -1e9;
    // 3D memo table initialized to null: memo[r1][c1][r2]
    const memo = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(n).fill(null))
    );

    const dp = (r1, c1, r2) => {
        const c2 = r1 + c1 - r2;
        if (
            r1 >= n || c1 >= n || r2 >= n || c2 >= n ||
            grid[r1][c1] === -1 || grid[r2][c2] === -1
        ) {
            return NEG_INF;
        }

        if (r1 === n - 1 && c1 === n - 1) {
            return grid[r1][c1];
        }

        if (memo[r1][c1][r2] !== null) {
            return memo[r1][c1][r2];
        }

        let cherries = grid[r1][c1];
        if (r1 !== r2 || c1 !== c2) {
            cherries += grid[r2][c2];
        }

        const bestNext = Math.max(
            dp(r1 + 1, c1, r2 + 1), // Both Down
            dp(r1 + 1, c1, r2),     // W1 Down, W2 Right
            dp(r1, c1 + 1, r2 + 1), // W1 Right, W2 Down
            dp(r1, c1 + 1, r2)      // Both Right
        );

        memo[r1][c1][r2] = cherries + bestNext;
        return memo[r1][c1][r2];
    };

    return Math.max(0, dp(0, 0, 0));
};
