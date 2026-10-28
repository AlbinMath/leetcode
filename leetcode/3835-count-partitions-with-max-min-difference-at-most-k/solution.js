/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPartitions = function (nums, k) {
    const MOD = 1000000007;
    const n = nums.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0;      // smallest valid start index (0-indexed into nums)
    let sum = 1;    // sum of dp[l..i-1], starts as dp[0]

    for (let i = 1; i <= n; i++) {
        const r = i - 1;
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while (nums[maxQ[maxH]] - nums[minQ[minH]] > k) {
            sum = (sum - dp[l] + MOD) % MOD;
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }

        dp[i] = sum;
        sum = (sum + dp[i]) % MOD;
    }
    return dp[n];
};
