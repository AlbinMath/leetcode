/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} score
 * @return {number}
 */
var maxProfit = function (n, edges, score) {
    const pre = new Int32Array(n);
    for (const [u, v] of edges) pre[v] |= 1 << u;

    const size = 1 << n;
    const dp = new Int32Array(size).fill(-1);
    const pc = new Uint8Array(size);
    for (let m = 1; m < size; m++) pc[m] = pc[m >> 1] + (m & 1);

    dp[0] = 0;
    for (let mask = 0; mask < size; mask++) {
        if (dp[mask] < 0) continue;
        const pos = pc[mask] + 1;
        for (let v = 0; v < n; v++) {
            if ((mask >> v) & 1) continue;
            if ((pre[v] & mask) !== pre[v]) continue;
            const nm = mask | (1 << v);
            const val = dp[mask] + score[v] * pos;
            if (val > dp[nm]) dp[nm] = val;
        }
    }
    return dp[size - 1];
};
