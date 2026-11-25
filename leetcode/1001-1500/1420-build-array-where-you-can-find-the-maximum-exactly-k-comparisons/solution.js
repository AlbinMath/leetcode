
var numOfArrays = function(n, m, k) {
    const MOD = 1000000007;

    if (k > n || k > m || k === 0) return 0;
    let dp = Array.from({ length: m + 1 }, () =>
        Array(k + 1).fill(0)
    );
    for (let j = 1; j <= m; j++) {
        dp[j][1] = 1;
    }
    for (let len = 2; len <= n; len++) {
        let next = Array.from({ length: m + 1 }, () =>
            Array(k + 1).fill(0)
        );

        for (let cost = 1; cost <= k; cost++) {
            let prefix = 0;

            for (let maxVal = 1; maxVal <= m; maxVal++) {
                if (maxVal > 1) {
                    prefix = (prefix + dp[maxVal - 1][cost - 1]) % MOD;
                }
                next[maxVal][cost] =
                    (dp[maxVal][cost] * maxVal + prefix) % MOD;
            }
        }

        dp = next;
    }
    let answer = 0;

    for (let maxVal = 1; maxVal <= m; maxVal++) {
        answer = (answer + dp[maxVal][k]) % MOD;
    }

    return answer;
};

