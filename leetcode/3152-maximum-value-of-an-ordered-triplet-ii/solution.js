
var maximumTripletValue = function(nums) {
    let leftMax = nums[0];
    let maxDiff = 0;
    let ans = 0;

    for (let k = 1; k < nums.length; k++) {
        ans = Math.max(ans, maxDiff * nums[k]);
        maxDiff = Math.max(maxDiff, leftMax - nums[k]);
        leftMax = Math.max(leftMax, nums[k]);
    }

    return ans;
};

