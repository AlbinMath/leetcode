/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const n = nums.length;
    let maxSum = 0;

    // Try every possible base k (1-indexed)
    for (let k = 1; k <= n; k++) {
        let currentSum = 0;
        
        // Multiply k by consecutive squares: 1^2, 2^2, 3^2, ...
        for (let j = 1; k * j * j <= n; j++) {
            const idx = k * j * j - 1; // Convert 1-indexed to 0-indexed
            currentSum += nums[idx];
        }
        
        if (currentSum > maxSum) {
            maxSum = currentSum;
        }
    }

    return maxSum;
};
