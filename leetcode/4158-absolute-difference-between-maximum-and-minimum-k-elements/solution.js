
var absDifference = function(nums, k) {
    nums.sort((a, b) => a - b);

    let smallestSum = 0;
    let largestSum = 0;
    const n = nums.length;

    for (let i = 0; i < k; i++) {
        smallestSum += nums[i];
        largestSum += nums[n - 1 - i];
    }

    return Math.abs(largestSum - smallestSum);
};

