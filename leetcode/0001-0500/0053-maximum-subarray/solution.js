var maxSubArray = function(nums) {
    let currentSum = nums[0];
    let maxSum = nums[0];

    for (let i = 1; i < nums.length; i++) {
        // Extend the current subarray or start a new one
        currentSum = Math.max(nums[i], currentSum + nums[i]);

        // Update the maximum sum found so far
        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
};
