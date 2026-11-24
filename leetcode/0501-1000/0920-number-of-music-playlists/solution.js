var numMusicPlaylists = function(n, goal, k) {
    const MOD = 1_000_000_007;
    const dp = Array.from(
        { length: goal + 1 },
        () => new Array(n + 1).fill(0)
    );

    dp[0][0] = 1;

    for (let i = 1; i <= goal; i++) {
        for (let j = 1; j <= n; j++) {
            // Play a new song that has not been used before.
            dp[i][j] = (dp[i - 1][j - 1] * (n - j + 1)) % MOD;

            // Replay a song that is not among the last k songs.
            if (j > k) {
                dp[i][j] = (
                    dp[i][j] + dp[i - 1][j] * (j - k)
                ) % MOD;
            }
        }
    }

    return dp[goal][n];
};
