var numberOfSets = function(n, k) {
    const MOD = 1000000007;

    // dp[j] = number of ways to choose j non-overlapping segments
    const dp = Array(k + 1).fill(0);
    dp[0] = 1;

    // prefix[j] stores cumulative dp[j]
    const prefix = Array(k + 1).fill(0);

    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            prefix[j] = (prefix[j] + dp[j - 1]) % MOD;
        }

        for (let j = 1; j <= k; j++) {
            dp[j] = (dp[j] + prefix[j]) % MOD;
        }
    }

    return dp[k];
};
