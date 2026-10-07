var minDistance = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;

    const dp = Array.from(
        { length: m + 1 },
        () => Array(n + 1).fill(0)
    );

    // Convert word1[0..i] to an empty string
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }

    // Convert empty string to word2[0..j]
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {

            if (word1[i - 1] === word2[j - 1]) {
                // Characters already match
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Insert, Delete, Replace
                dp[i][j] = 1 + Math.min(
                    dp[i][j - 1],     // Insert
                    dp[i - 1][j],     // Delete
                    dp[i - 1][j - 1]  // Replace
                );
            }
        }
    }

    return dp[m][n];
};
