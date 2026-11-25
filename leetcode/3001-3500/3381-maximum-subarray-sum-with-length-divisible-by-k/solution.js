
var maxSubarraySum = function(nums, k) {
    const minPrefix = new Array(k).fill(Infinity);
    minPrefix[0] = 0;

    let prefixSum = 0;
    let ans = -Infinity;

    for (let i = 0; i < nums.length; i++) {
        prefixSum += nums[i];
        const remainder = (i + 1) % k;
        ans = Math.max(
            ans,
            prefixSum - minPrefix[remainder]
        );
        minPrefix[remainder] = Math.min(
            minPrefix[remainder],
            prefixSum
        );
    }

    return ans;
};

