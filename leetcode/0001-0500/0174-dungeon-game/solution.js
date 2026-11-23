var calculateMinimumHP = function(dungeon) {
    const m = dungeon.length;
    const n = dungeon[0].length;
    // dp[c] = min HP required upon entering cell (r, c)
    const dp = new Array(n + 1).fill(Infinity);
    dp[n - 1] = 1; // Need at least 1 HP after surviving the princess's room

    for (let r = m - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            const minHpOnExit = Math.min(dp[c], dp[c + 1]);
            dp[c] = Math.max(1, minHpOnExit - dungeon[r][c]);
        }
    }

    return dp[0];
};
