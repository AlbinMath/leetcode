/**
 * @param {number[]} chargeTimes
 * @param {number[]} runningCosts
 * @param {number} budget
 * @return {number}
 */
var maximumRobots = function (chargeTimes, runningCosts, budget) {
    const n = chargeTimes.length;
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let l = 0, sum = 0, ans = 0;

    for (let r = 0; r < n; r++) {
        sum += runningCosts[r];
        while (head < tail && chargeTimes[dq[tail - 1]] <= chargeTimes[r]) tail--;
        dq[tail++] = r;

        while (head < tail && chargeTimes[dq[head]] + (r - l + 1) * sum > budget) {
            sum -= runningCosts[l];
            if (dq[head] === l) head++;
            l++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};
