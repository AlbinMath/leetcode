
var subarraySum = function(nums) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    let ans = 0;

    for (let i = 0; i < n; i++) {
        const start = Math.max(0, i - nums[i]);
        const sum = prefix[i + 1] - prefix[start];

        ans += sum;
    }

    return ans;
};

