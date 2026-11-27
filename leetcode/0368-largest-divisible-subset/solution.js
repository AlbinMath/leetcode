
var largestDivisibleSubset = function(nums) {
    nums.sort((a, b) => a - b);

    const n = nums.length;
    const dp = new Array(n).fill(1);
    const prev = new Array(n).fill(-1);

    let maxLength = 1;
    let lastIndex = 0;

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }

        if (dp[i] > maxLength) {
            maxLength = dp[i];
            lastIndex = i;
        }
    }

    const result = [];

    while (lastIndex !== -1) {
        result.push(nums[lastIndex]);
        lastIndex = prev[lastIndex];
    }

    return result.reverse();
};

