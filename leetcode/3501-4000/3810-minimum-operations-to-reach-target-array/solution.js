var minOperations = function(nums, target) {
    const seen = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== target[i]) {
            seen.add(nums[i]);
        }
    }

    return seen.size;
};
