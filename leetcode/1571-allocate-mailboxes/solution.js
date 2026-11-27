
var minDistance = function(houses, k) {
    houses.sort((a, b) => a - b);

    const n = houses.length;

    const cost = Array.from({ length: n }, () => 
        new Array(n).fill(0)
    );

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const mid = Math.floor((i + j) / 2);
            cost[i][j] = cost[i][j - 1] + houses[j] - houses[mid];
        }
    }

    const dp = Array.from({ length: n + 1 }, () =>
        new Array(k + 1).fill(Infinity)
    );

    dp[0][0] = 0;

    for (let i = 1; i <= n; i++) {
        for (let m = 1; m <= Math.min(i, k); m++) {
            for (let j = 0; j < i; j++) {
                dp[i][m] = Math.min(
                    dp[i][m],
                    dp[j][m - 1] + cost[j][i - 1]
                );
            }
        }
    }

    return dp[n][k];
};

