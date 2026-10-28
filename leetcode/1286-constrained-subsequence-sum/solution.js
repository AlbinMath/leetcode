/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var constrainedSubsetSum = function (nums, k) {
    const n = nums.length;
    const dp = new Array(n);
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = -Infinity;

    for (let i = 0; i < n; i++) {
        if (head < tail && dq[head] < i - k) head++;

        const best = head < tail ? Math.max(0, dp[dq[head]]) : 0;
        dp[i] = nums[i] + best;
        ans = Math.max(ans, dp[i]);

        while (head < tail && dp[dq[tail - 1]] <= dp[i]) tail--;
        dq[tail++] = i;
    }
    return ans;
};
