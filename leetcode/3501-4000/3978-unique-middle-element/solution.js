
var isMiddleElementUnique = function(nums) {
    const mid = Math.floor(nums.length / 2);
    const middle = nums[mid];

    let count = 0;

    for (const num of nums) {
        if (num === middle) {
            count++;
        }
    }

    return count === 1;
};

