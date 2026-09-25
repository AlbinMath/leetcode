/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    // Total sum - x = sum of the subarray we want to KEEP
    const total = nums.reduce((sum, num) => sum + num, 0);
    const target = total - x;

    if (target < 0) return -1;
    if (target === 0) return nums.length;

    let left = 0;
    let sum = 0;
    let maxLength = -1;

    // Sliding window to find the longest subarray
    // whose sum is equal to target
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum > target && left <= right) {
            sum -= nums[left];
            left++;
        }

        if (sum === target) {
            maxLength = Math.max(maxLength, right - left + 1);
        }
    }

    return maxLength === -1 ? -1 : nums.length - maxLength;
};
