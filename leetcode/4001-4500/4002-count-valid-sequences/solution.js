/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countValidSequences = function (n, k) {
    const MOD = 1000000007n;

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

    // factorials up to n
    const fact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;

    const invFact = new Array(n + 1);
    invFact[n] = power(fact[n], MOD - 2n);
    for (let i = n; i >= 1; i--) invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;

    const comb = (a, b) => {
        if (b < 0 || b > a || a < 0) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    const total = comb(n - 1, k - 1);

    let allOdd = 0n;
    const diff = n - k;
    if (diff >= 0 && diff % 2 === 0) {
        allOdd = comb(diff / 2 + k - 1, k - 1);
    }

    return Number(((total - allOdd) % MOD + MOD) % MOD);
};
