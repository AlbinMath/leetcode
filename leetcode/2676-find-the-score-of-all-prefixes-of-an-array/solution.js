
var findPrefixScore = function(nums) {
    let n = nums.length;
    let ans = new Array(n);
    let maxValue = 0;
    let score = 0;

    for (let i = 0; i < n; i++) {
        maxValue = Math.max(maxValue, nums[i]);
        let conver = nums[i] + maxValue;
        score += conver;
        ans[i] = score;
    }
    return ans;
};

