
var countPartitions = function(nums) {
    const totalSum = nums.reduce((sum, num) => sum + num, 0);

    if (totalSum % 2 === 0) {
        return nums.length - 1;
    }

    return 0;
};

