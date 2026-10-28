/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var countGoodArrays = function (n, m, k) {
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

    // Factorials up to n - 1
    const fact = new Array(n).fill(1n);
    for (let i = 1; i < n; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // C(n-1, k) = (n-1)! / (k! * (n-1-k)!)
    const comb =
        (fact[n - 1] *
            power(fact[k], MOD - 2n) % MOD *
            power(fact[n - 1 - k], MOD - 2n)) %
        MOD;

    const ways = (BigInt(m) * power(BigInt(m - 1), BigInt(n - k - 1))) % MOD;

    return Number((comb * ways) % MOD);
};
