var triangleNumber = function(nums) {
    nums.sort((a, b) => a - b);

    let count = 0;
    const n = nums.length;

    for (let k = n - 1; k >= 2; k--) {
        let left = 0;
        let right = k - 1;

        while (left < right) {
            if (nums[left] + nums[right] > nums[k]) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }
    }

    return count;
};
