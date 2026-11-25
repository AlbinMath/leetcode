
var maximumStrength = function(nums, k) {
    const dp = new Array(k + 1).fill(-Infinity);
    const ending = new Array(k + 1).fill(-Infinity);
    dp[0] = 0;

    for (let num of nums) {
        for (let j = k; j >= 1; j--) {

            const weight = (j % 2 === 1 ? 1 : -1) * (k - j + 1);
            ending[j] = Math.max(
                ending[j],
                dp[j - 1]
            ) + weight * num;
            dp[j] = Math.max(dp[j], ending[j]);
        }
    }

    return dp[k];
};

