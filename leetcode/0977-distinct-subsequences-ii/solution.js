/**
 * @param {string} s
 * @return {number}
 */
var distinctSubseqII = function(s) {
    const MOD = 1000000007;
    let dp = 1;
    const last = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        let newDp = (2 * dp) % MOD;
        newDp = (newDp - last[c] + MOD) % MOD;
        last[c] = dp;
        dp = newDp;
    }
    return (dp - 1 + MOD) % MOD;
};
