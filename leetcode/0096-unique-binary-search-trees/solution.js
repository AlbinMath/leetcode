
var numTrees = function(n) {
    const dp = new Array(n + 1).fill(0);

    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        for (let root = 1; root <= i; root++) {
            dp[i] += dp[root - 1] * dp[i - root];
        }
    }

    return dp[n];
};

