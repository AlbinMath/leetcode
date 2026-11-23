var countOfPairs = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    let dp = new Array(nums[0] + 1).fill(1);

    for (let i = 1; i < n; i++) {
        const prev = dp;
        const curr = new Array(nums[i] + 1).fill(0);
        const diff = Math.max(0, nums[i] - nums[i - 1]);

        let prefix = 0;

        for (let j = 0; j <= nums[i]; j++) {
            if (j - diff >= 0 && j - diff < prev.length) {
                prefix = (prefix + prev[j - diff]) % MOD;
            }

            curr[j] = prefix;
        }

        dp = curr;
    }

    return dp.reduce((sum, ways) => (sum + ways) % MOD, 0);
};
