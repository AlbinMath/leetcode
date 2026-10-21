
var minDistance = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;

    const dp = Array.from(
        { length: m + 1 },
        () => Array(n + 1).fill(0)
    );

    // Convert word1's first i characters to an empty string.
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }

    // Convert an empty string to word2's first j characters.
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (word1[i - 1] === word2[j - 1]) {
                // Characters match; no operation is needed.
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Choose the cheapest operation.
                const insert = dp[i][j - 1];
                const deleteChar = dp[i - 1][j];
                const replace = dp[i - 1][j - 1];

                dp[i][j] = 1 + Math.min(
                    insert,
                    deleteChar,
                    replace
                );
            }
        }
    }

    return dp[m][n];
};

