/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function (stations, r, k) {
    const n = stations.length;

    // initial power of each city via prefix sums
    const pre = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pre[i + 1] = pre[i] + stations[i];
    const power = new Array(n);
    let mn = Infinity;
    for (let i = 0; i < n; i++) {
        const lo = Math.max(0, i - r);
        const hi = Math.min(n - 1, i + r);
        power[i] = pre[hi + 1] - pre[lo];
        if (power[i] < mn) mn = power[i];
    }

    const check = (x) => {
        const end = new Array(n + 1).fill(0); // end[i]: amount that stops covering at i
        let added = 0, used = 0;
        for (let i = 0; i < n; i++) {
            added -= end[i];
            const cur = power[i] + added;
            if (cur < x) {
                const need = x - cur;
                used += need;
                if (used > k) return false;
                added += need;
                const stop = i + 2 * r + 1;
                if (stop < n) end[stop] += need;
            }
        }
        return true;
    };

    let lo = mn, hi = mn + k;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (check(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
