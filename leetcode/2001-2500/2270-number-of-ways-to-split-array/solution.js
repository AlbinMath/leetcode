
var waysToSplitArray = function(nums) {
    const n = nums.length;
    let totalSum = 0;
    for (let num of nums) {
        totalSum += num;
    }
    let leftSum = 0;
    let count = 0;
    for (let i = 0; i < n - 1; i++) {
        leftSum += nums[i];
        let rightSum = totalSum - leftSum;
        if (leftSum >= rightSum) {
            count++;
        }
    }
    return count;
};

