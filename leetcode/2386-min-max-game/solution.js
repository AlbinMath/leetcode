var minMaxGame = function(nums) {
    let n = nums.length;
    
    while (n > 1) {
        const half = n >> 1;
        for (let i = 0; i < half; i++) {
            if (i % 2 === 0) {
                nums[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
            } else {
                nums[i] = Math.max(nums[2 * i], nums[2 * i + 1]);
            }
        }
        n = half;
    }
    
    return nums[0];
};
