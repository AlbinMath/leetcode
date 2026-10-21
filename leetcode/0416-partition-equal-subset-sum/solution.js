
var canPartition = function(nums) {
    const total = nums.reduce((sum, num) => sum + num, 0);

    // An odd sum cannot be divided equally
    if (total % 2 !== 0) {
        return false;
    }

    const target = total / 2;
    const dp = Array(target + 1).fill(false);

    dp[0] = true;

    for (const num of nums) {
        // Iterate backward to use each number only once
        for (let sum = target; sum >= num; sum--) {
            dp[sum] = dp[sum] || dp[sum - num];
        }

        if (dp[target]) {
            return true;
        }
    }

    return dp[target];
};

