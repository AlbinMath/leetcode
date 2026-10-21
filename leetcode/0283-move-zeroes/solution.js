var moveZeroes = function(nums) {
    let position = 0;

    // Move all non-zero elements to the front
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            [nums[position], nums[i]] = [nums[i], nums[position]];
            position++;
        }
    }
};
