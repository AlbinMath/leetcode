var countOfPairs = function(nums) {
    const MOD = 1000000007;
    const maxVal = Math.max(...nums);

    let dp = new Array(maxVal + 1).fill(0);

    for (let j = 0; j <= nums[0]; j++) {
        dp[j] = 1;
    }

    for (let i = 1; i < nums.length; i++) {
        const next = new Array(maxVal + 1).fill(0);
        const diff = Math.max(0, nums[i] - nums[i - 1]);
        let prefix = 0;

        for (let j = 0; j <= nums[i]; j++) {
            if (j - diff >= 0) {
                prefix = (prefix + dp[j - diff]) % MOD;
            }
            next[j] = prefix;
        }

        dp = next;
    }

    let ans = 0;
    for (let j = 0; j <= nums[nums.length - 1]; j++) {
        ans = (ans + dp[j]) % MOD;
    }

    return ans;
};
