/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumLength = function (nums) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    const dp = new Array(n + 1).fill(0);
    const key = new Array(n + 1).fill(0); // key[j] = P[j] + last[j]
    const dq = new Array(n + 1);
    let head = 0, tail = 0;
    dq[tail++] = 0;

    for (let i = 1; i <= n; i++) {
        while (tail - head >= 2 && key[dq[head + 1]] <= P[i]) head++;
        const j = dq[head];
        dp[i] = dp[j] + 1;
        key[i] = P[i] + (P[i] - P[j]);
        while (head < tail && key[dq[tail - 1]] >= key[i]) tail--;
        dq[tail++] = i;
    }
    return dp[n];
};
