var subsequenceSumAfterCapping = function(nums, k) {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0);
    for (const num of nums) {
        freq[num]++;
    }
    const dp = new Array(k + 1).fill(false);
    dp[0] = true;
    const answer = new Array(n).fill(false);
    let largeCount = n;
    for (let x = 1; x <= n; x++) {
        const maxTake = Math.min(largeCount, Math.floor(k / x));
        for (let t = 0; t <= maxTake; t++) {
            const remaining = k - t * x;
            if (dp[remaining]) {
                answer[x - 1] = true;
                break;
            }
        }
        largeCount -= freq[x];
        for (let j = 0; j < freq[x]; j++) {
            for (let sum = k; sum >= x; sum--) {
                if (dp[sum - x]) {
                    dp[sum] = true;
                }
            }
        }
    }
    return answer;
};

