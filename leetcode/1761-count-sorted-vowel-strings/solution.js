var countVowelStrings = function(n) {
    let dp = [1, 1, 1, 1, 1];

    for (let i = 2; i <= n; i++) {
        for (let j = 3; j >= 0; j--) {
            dp[j] += dp[j + 1];
        }
    }

    return dp.reduce((sum, count) => sum + count, 0);
};
