var findPeakElement = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] < nums[mid + 1]) {
            // Peak is on the right side
            left = mid + 1;
        } else {
            // Peak is at mid or on the left side
            right = mid;
        }
    }

    return left;
};
