/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    const m = s.length;
    const n = t.length;

    // dp[j] = number of ways to form t[0...j-1]
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= m; i++) {
        // Go backwards so we don't overwrite values
        for (let j = n; j >= 1; j--) {
            if (s[i - 1] === t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }

    return dp[n];
};
