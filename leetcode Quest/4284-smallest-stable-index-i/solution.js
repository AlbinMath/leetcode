/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var firstStableIndex = function(nums, k) {
    let n = nums.length;

    // Suffix minimums
    let suffixMin = new Array(n);
    suffixMin[n - 1] = nums[n - 1];

    for (let i = n - 2; i >= 0; i--) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }

    // Prefix maximum
    let prefixMax = nums[0];

    for (let i = 0; i < n; i++) {
        prefixMax = Math.max(prefixMax, nums[i]);

        let instability = prefixMax - suffixMin[i];

        if (instability <= k) {
            return i;
        }
    }

    return -1;
};
