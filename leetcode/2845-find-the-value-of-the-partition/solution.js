
var findValueOfPartition = function(nums) {
    nums.sort((a, b) => a - b);

    let minDiff = Infinity;

    for (let i = 1; i < nums.length; i++) {
        let diff = nums[i] - nums[i - 1];

        minDiff = Math.min(minDiff, diff);
    }

    return minDiff;
};

