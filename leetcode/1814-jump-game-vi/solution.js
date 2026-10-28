/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxResult = function (nums, k) {
    const n = nums.length;
    const dp = new Array(n);
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]

    dp[0] = nums[0];
    dq[tail++] = 0;

    for (let i = 1; i < n; i++) {
        while (dq[head] < i - k) head++;      // drop indices outside the window
        dp[i] = nums[i] + dp[dq[head]];
        while (head < tail && dp[dq[tail - 1]] <= dp[i]) tail--;
        dq[tail++] = i;
    }
    return dp[n - 1];
};
