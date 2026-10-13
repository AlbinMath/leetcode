var numSubseq = function(nums, target) {
    const MOD = 1000000007;
    nums.sort((a, b) => a - b);

    const n = nums.length;
    const pow2 = new Array(n);

    pow2[0] = 1;

    for (let i = 1; i < n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    let left = 0;
    let right = n - 1;
    let count = 0;

    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            count = (count + pow2[right - left]) % MOD;
            left++;
        } else {
            right--;
        }
    }

    return count;
};
