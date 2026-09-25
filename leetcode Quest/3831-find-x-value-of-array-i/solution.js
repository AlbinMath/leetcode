/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var resultArray = function(nums, k) {
    const result = new Array(k).fill(0);

    // dp[r] = number of subarrays ending at previous position
    // whose product % k == r
    let dp = new Array(k).fill(0);

    for (const num of nums) {
        const x = num % k;
        const next = new Array(k).fill(0);

        // Subarray consisting only of the current element
        next[x]++;

        // Extend every previous subarray
        for (let r = 0; r < k; r++) {
            if (dp[r] > 0) {
                const newRemainder = (r * x) % k;
                next[newRemainder] += dp[r];
            }
        }

        // All subarrays ending here contribute to the answer
        for (let r = 0; r < k; r++) {
            result[r] += next[r];
        }

        dp = next;
    }

    return result;
};
