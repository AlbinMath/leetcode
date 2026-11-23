var applyOperations = function(nums) {
    const n = nums.length;

    // Step 1: Apply sequential operations
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }

    // Step 2: Shift all zeros to the end in-place
    let writeIdx = 0;
    for (let readIdx = 0; readIdx < n; readIdx++) {
        if (nums[readIdx] !== 0) {
            [nums[writeIdx], nums[readIdx]] = [nums[readIdx], nums[writeIdx]];
            writeIdx++;
        }
    }

    return nums;
};
