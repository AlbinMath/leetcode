/**
 * @param {number[]} prices
 * @return {number}
 */
var minimumCoins = function (prices) {
    const n = prices.length;
    const dp = new Array(n + 2).fill(0); // 1-indexed

    for (let i = n; i >= 1; i--) {
        if (2 * i >= n) {
            dp[i] = prices[i - 1];
        } else {
            let best = Infinity;
            for (let j = i + 1; j <= 2 * i + 1; j++) {
                if (dp[j] < best) best = dp[j];
            }
            dp[i] = prices[i - 1] + best;
        }
    }
    return dp[1];
};
