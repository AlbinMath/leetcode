var singleNonDuplicate = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        // Ensure mid is even
        if (mid % 2 === 1) {
            mid--;
        }

        if (nums[mid] === nums[mid + 1]) {
            // Single element is in the right half
            left = mid + 2;
        } else {
            // Single element is in the left half, including mid
            right = mid;
        }
    }

    return nums[left];
};
