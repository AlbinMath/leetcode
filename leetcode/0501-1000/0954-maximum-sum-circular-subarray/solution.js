
var maxSubarraySumCircular = function(nums) {
    let totalSum = 0;

    let currentMax = 0;
    let maxSum = -Infinity;

    let currentMin = 0;
    let minSum = Infinity;

    for (const num of nums) {
        totalSum += num;

        // Maximum subarray (Kadane's algorithm)
        currentMax = Math.max(num, currentMax + num);
        maxSum = Math.max(maxSum, currentMax);

        // Minimum subarray
        currentMin = Math.min(num, currentMin + num);
        minSum = Math.min(minSum, currentMin);
    }

    // If every number is negative, wrapping would give 0,
    // which is invalid because the subarray must be non-empty.
    if (maxSum < 0) {
        return maxSum;
    }

    return Math.max(maxSum, totalSum - minSum);
};

