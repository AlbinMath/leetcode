var arrayChange = function(nums, operations) {
    // Map each distinct value to its current index in nums
    const pos = new Map();
    for (let i = 0; i < nums.length; i++) {
        pos.set(nums[i], i);
    }

    for (const [oldVal, newVal] of operations) {
        const idx = pos.get(oldVal);
        pos.delete(oldVal);
        nums[idx] = newVal;
        pos.set(newVal, idx);
    }

    return nums;
};
