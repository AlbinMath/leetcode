
var goodIndices = function(nums, k) {
    const n = nums.length;

    let left = new Array(n).fill(1);
    let right = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (nums[i] <= nums[i - 1]) {
            left[i] = left[i - 1] + 1;
        }
    }
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) {
            right[i] = right[i + 1] + 1;
        }
    }

    let result = [];
    for (let i = k; i < n - k; i++) {
        if (left[i - 1] >= k && right[i + 1] >= k) {
            result.push(i);
        }
    }

    return result;
};

