/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var maximumSum = function (nums, m, l, r) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    // f(1): best single subarray with length in [l, r]
    let f1 = -Infinity;
    {
        const dq = new Array(n + 1);
        let h = 0, t = 0;
        for (let i = l; i <= n; i++) {
            const s = i - l;
            while (h < t && P[dq[t - 1]] >= P[s]) t--;
            dq[t++] = s;
            while (dq[h] < i - r) h++;
            f1 = Math.max(f1, P[i] - P[dq[h]]);
        }
    }
    if (f1 <= 0) return f1;

    const dpV = new Float64Array(n + 1);
    const dpC = new Int32Array(n + 1);
    const kv = new Float64Array(n + 1);
    const dq = new Int32Array(n + 1);

    // returns [best value of sum - lambda*count, min count achieving it]
    const run = (lambda) => {
        let h = 0, t = 0;
        dpV[0] = 0; dpC[0] = 0;
        for (let i = 1; i <= n; i++) {
            const s = i - l;
            if (s >= 0) {
                kv[s] = dpV[s] - P[s];
                while (t > h) {
                    const b = dq[t - 1];
                    if (kv[s] > kv[b] || (kv[s] === kv[b] && dpC[s] <= dpC[b])) t--;
                    else break;
                }
                dq[t++] = s;
            }
            while (h < t && dq[h] < i - r) h++;

            dpV[i] = dpV[i - 1];
            dpC[i] = dpC[i - 1];
            if (h < t) {
                const f = dq[h];
                const cv = kv[f] + P[i] - lambda;
                const cc = dpC[f] + 1;
                if (cv > dpV[i] || (cv === dpV[i] && cc < dpC[i])) {
                    dpV[i] = cv;
                    dpC[i] = cc;
                }
            }
        }
        return [dpV[n], dpC[n]];
    };

    let lo = 0, hi = 1e10 + 1; // at hi, no subarray is worth taking (count 0)
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (run(mid)[1] <= m) hi = mid;
        else lo = mid + 1;
    }
    const [v] = run(lo);
    return v + lo * m;
};
