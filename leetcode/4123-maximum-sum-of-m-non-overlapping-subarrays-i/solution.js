/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var maximumSum = function (nums, m, l, r) {
    const n = nums.length;
    const NEG = -Infinity;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    let prev = new Array(n + 1).fill(0); // j = 0: zero subarrays, sum 0
    let ans = NEG;

    for (let j = 1; j <= m; j++) {
        const cur = new Array(n + 1).fill(NEG);
        const dq = new Array(n + 1);
        let head = 0, tail = 0;

        for (let i = 1; i <= n; i++) {
            const s = i - l; // newly eligible start boundary
            if (s >= 0 && prev[s] !== NEG) {
                const v = prev[s] - P[s];
                while (head < tail && prev[dq[tail - 1]] - P[dq[tail - 1]] <= v) tail--;
                dq[tail++] = s;
            }
            while (head < tail && dq[head] < i - r) head++;

            cur[i] = cur[i - 1];
            if (head < tail) {
                const cand = P[i] + prev[dq[head]] - P[dq[head]];
                if (cand > cur[i]) cur[i] = cand;
            }
        }
        if (cur[n] > ans) ans = cur[n];
        prev = cur;
    }
    return ans;
};
