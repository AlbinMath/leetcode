var minSpaceWastedKResizing = function(nums, k) {
    const n = nums.length;
    const INF = Infinity;
    let prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let cost = Array.from(
        { length: n },
        () => new Array(n).fill(0)
    );
    for (let i = 0; i < n; i++) {
        let maxVal = 0;
        for (let j = i; j < n; j++) {
            maxVal = Math.max(maxVal, nums[j]);
            let sum = prefix[j + 1] - prefix[i];
            cost[i][j] = (j - i + 1) * maxVal - sum;
        }
    }
    let dp = Array.from(
        { length: n + 1 },
        () => new Array(k + 2).fill(INF)
    );
    dp[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let g = 1; g <= Math.min(i, k + 1); g++) {
            for (let j = g - 1; j < i; j++) {
                dp[i][g] = Math.min(
                    dp[i][g],
                    dp[j][g - 1] + cost[j][i - 1]
                );
            }
        }
    }
    let answer = INF;
    for (let g = 1; g <= k + 1; g++) {
        answer = Math.min(answer, dp[n][g]);
    }
    return answer;
};

