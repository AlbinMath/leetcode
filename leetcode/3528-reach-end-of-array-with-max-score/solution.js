
var findMaximumScore = function(nums) {
    let score = 0;
    let maxValue = nums[0];

    for (let i = 1; i < nums.length; i++) {
        score += maxValue;
        maxValue = Math.max(maxValue, nums[i]);
    }

    return score;
};

