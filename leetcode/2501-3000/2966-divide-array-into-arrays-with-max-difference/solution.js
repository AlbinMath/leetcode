
var divideArray = function(nums, k) {
    nums.sort((a, b) => a - b);

    const result = [];

    for (let i = 0; i < nums.length; i += 3) {
        // Check the difference between max and min
        if (nums[i + 2] - nums[i] > k) {
            return [];
        }

        result.push([
            nums[i],
            nums[i + 1],
            nums[i + 2]
        ]);
    }

    return result;
};

