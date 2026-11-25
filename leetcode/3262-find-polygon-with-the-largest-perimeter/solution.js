
var largestPerimeter = function(nums) {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    for (let i = nums.length - 1; i >= 2; i--) {
        let remainingSum = sum - nums[i];

        if (remainingSum > nums[i]) {
            return sum;
        }
        sum -= nums[i];
    }
    return -1;
};

