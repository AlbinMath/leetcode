var specialTriplets = function(nums) {
    const MOD = 1000000007;
    const MAX = 200001;

    let left = Array(MAX).fill(0);
    let right = Array(MAX).fill(0);

    // Count all elements initially in right
    for (const num of nums) {
        right[num]++;
    }

    let ans = 0;

    for (let j = 0; j < nums.length; j++) {
        let x = nums[j];
        let target = x * 2;

        // Remove current element from right
        right[x]--;

        // Count valid pairs on both sides
        ans = (ans + left[target] * right[target]) % MOD;

        // Add current element to left
        left[x]++;
    }

    return ans;
};
