/**
 * @param {number[][]} boxes
 * @param {number} portsCount
 * @param {number} maxBoxes
 * @param {number} maxWeight
 * @return {number}
 */
var boxDelivering = function (boxes, portsCount, maxBoxes, maxWeight) {
    const n = boxes.length;
    const neg = new Array(n).fill(0);   // neg[t] = port changes among boxes 0..t
    const W = new Array(n + 1).fill(0); // prefix weights
    for (let t = 0; t < n; t++) {
        W[t + 1] = W[t] + boxes[t][1];
        if (t >= 1) neg[t] = neg[t - 1] + (boxes[t][0] !== boxes[t - 1][0] ? 1 : 0);
    }

    const dp = new Array(n + 1).fill(0);
    const dq = new Array(n + 1);
    let head = 0, tail = 0;

    for (let i = 1; i <= n; i++) {
        const j = i - 1;
        const val = dp[j] - neg[j];
        while (head < tail && dp[dq[tail - 1]] - neg[dq[tail - 1]] >= val) tail--;
        dq[tail++] = j;

        while (i - dq[head] > maxBoxes || W[i] - W[dq[head]] > maxWeight) head++;

        const f = dq[head];
        dp[i] = (dp[f] - neg[f]) + neg[i - 1] + 2;
    }
    return dp[n];
};
