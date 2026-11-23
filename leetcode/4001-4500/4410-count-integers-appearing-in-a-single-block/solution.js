
var countSpecialIntegers = function(nums) {
    let blocks = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) {
            blocks.set(nums[i], (blocks.get(nums[i]) || 0) + 1);
        }
    }

    let count = 0;

    for (let [num, freq] of blocks) {
        if (freq === 1) {
            count++;
        }
    }

    return count;
};

