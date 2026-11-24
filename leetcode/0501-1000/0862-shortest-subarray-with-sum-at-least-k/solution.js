/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var shortestSubarray = function (nums, k) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    const dq = new Array(n + 1);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = Infinity;

    for (let j = 0; j <= n; j++) {
        while (head < tail && P[j] - P[dq[head]] >= k) {
            ans = Math.min(ans, j - dq[head]);
            head++;
        }
        while (head < tail && P[dq[tail - 1]] >= P[j]) {
            tail--;
        }
        dq[tail++] = j;
    }

    return ans === Infinity ? -1 : ans;
};
