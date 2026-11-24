/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minMaxSums = function (nums, k) {
    const MOD = 1000000007n;
    const n = nums.length;
    nums.sort((a, b) => a - b);

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

    // Factorials and inverse factorials up to n
    const fact = new Array(n + 1).fill(1n);
    for (let i = 1; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    const invFact = new Array(n + 1).fill(1n);
    invFact[n] = power(fact[n], MOD - 2n);
    for (let i = n; i > 0; i--) invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;

    const comb = (a, b) => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    // sum_{j=0}^{k-1} C(x, j)
    const countUpTo = (x) => {
        let s = 0n;
        for (let j = 0; j < k && j <= x; j++) s += comb(x, j);
        return s % MOD;
    };

    let ans = 0n;
    for (let i = 0; i < n; i++) {
        const cnt = (countUpTo(i) + countUpTo(n - 1 - i)) % MOD;
        ans = (ans + BigInt(nums[i]) * cnt) % MOD;
    }
    return Number(ans);
};
