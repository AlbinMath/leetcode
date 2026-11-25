var maxSumRangeQuery = function(nums, requests) {
    const MOD = 1000000007;
    const n = nums.length;
    let diff = new Array(n + 1).fill(0);
    for (let [start, end] of requests) {
        diff[start]++;
        diff[end + 1]--;
    }
    let freq = new Array(n).fill(0);
    let current = 0;

    for (let i = 0; i < n; i++) {
        current += diff[i];
        freq[i] = current;
    }
    nums.sort((a, b) => a - b);
    freq.sort((a, b) => a - b);
    let result = 0;

    for (let i = 0; i < n; i++) {
        result = (result + nums[i] * freq[i]) % MOD;
    }

    return result;
};
