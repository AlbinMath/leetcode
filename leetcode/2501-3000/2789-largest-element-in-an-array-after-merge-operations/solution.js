var maxArrayValue = function(nums) {
    let sum = nums[nums.length - 1];
    let max = sum;

    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] <= sum) {
            sum += nums[i];
        } else {
            sum = nums[i];
        }

        max = Math.max(max, sum);
    }

    return max;
};
