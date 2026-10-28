/**
 * @param {number} n
 * @param {number} delay
 * @param {number} forget
 * @return {number}
 */
var peopleAwareOfSecret = function (n, delay, forget) {
    const MOD = 1000000007;
    const nw = new Array(n + 1).fill(0);
    nw[1] = 1;
    let share = 0; // people able to share on the current day

    for (let d = 2; d <= n; d++) {
        if (d - delay >= 1) share = (share + nw[d - delay]) % MOD;
        if (d - forget >= 1) share = (share - nw[d - forget] + MOD) % MOD;
        nw[d] = share;
    }

    let ans = 0;
    for (let j = Math.max(1, n - forget + 1); j <= n; j++) {
        ans = (ans + nw[j]) % MOD;
    }
    return ans;
};
