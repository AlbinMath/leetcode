/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var distanceSum = function (m, n, k) {
    const MOD = 1000000007n;
    const N = m * n;

    const power = (base, exp) => {
        let result = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return result;
    };

    // Factorials up to N - 2
    const top = N - 2;
    const fact = new Array(top + 1).fill(1n);
    for (let i = 1; i <= top; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // C(N-2, k-2)
    const a = top, b = k - 2;
    const comb =
        (fact[a] *
            power(fact[b], MOD - 2n) % MOD *
            power(fact[a - b], MOD - 2n)) %
        MOD;

    // Sum over d of d * (len - d)
    const lineSum = (len) => {
        let s = 0n;
        for (let d = 1; d < len; d++) {
            s += BigInt(d) * BigInt(len - d);
        }
        return s % MOD;
    };

    const M = BigInt(m), Nn = BigInt(n);
    const pairSum =
        (Nn * Nn % MOD * lineSum(m) + M * M % MOD * lineSum(n)) % MOD;

    return Number(comb * pairSum % MOD);
};
