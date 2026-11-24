/**
 * @param {number} m
 * @param {number} k
 * @param {number[]} nums
 * @return {number}
 */
var magicalSum = function (m, k, nums) {
    const MOD = 1000000007;
    const MODn = 1000000007n;
    const len = nums.length;

    const mul = (a, b) =>
        (((a * (b >>> 16)) % MOD) * 65536 + a * (b & 65535)) % MOD;

    const power = (base, exp) => {
        let r = 1n;
        base %= MODn;
        while (exp > 0n) {
            if (exp & 1n) r = (r * base) % MODn;
            base = (base * base) % MODn;
            exp >>= 1n;
        }
        return r;
    };

    // factorials and inverse factorials up to m
    const fact = [1n];
    for (let i = 1; i <= m; i++) fact.push((fact[i - 1] * BigInt(i)) % MODn);
    const invFact = fact.map((f) => power(f, MODn - 2n));

    // coef[i][c] = nums[i]^c / c!
    const coef = [];
    for (let i = 0; i < len; i++) {
        const row = [];
        let p = 1n;
        const base = BigInt(nums[i]) % MODn;
        for (let c = 0; c <= m; c++) {
            row.push(Number((p * invFact[c]) % MODn));
            p = (p * base) % MODn;
        }
        coef.push(row);
    }

    const C = m + 1; // carry never exceeds m
    const K = k + 1;
    const idx = (j, c, o) => (j * C + c) * K + o;
    const size = (m + 1) * C * K;

    let dp = new Array(size).fill(0);
    dp[idx(0, 0, 0)] = 1;

    for (let i = 0; i < len; i++) {
        const nd = new Array(size).fill(0);
        const row = coef[i];
        for (let j = 0; j <= m; j++) {
            for (let c = 0; c <= j; c++) {
                for (let o = 0; o <= k; o++) {
                    const cur = dp[idx(j, c, o)];
                    if (cur === 0) continue;
                    for (let cnt = 0; j + cnt <= m; cnt++) {
                        const t = c + cnt;
                        const no = o + (t & 1);
                        if (no > k) continue;
                        const nc = t >> 1;
                        const id = idx(j + cnt, nc, no);
                        nd[id] = (nd[id] + mul(cur, row[cnt])) % MOD;
                    }
                }
            }
        }
        dp = nd;
    }

    const popcount = (x) => {
        let r = 0;
        while (x) {
            r += x & 1;
            x >>= 1;
        }
        return r;
    };

    let total = 0;
    for (let c = 0; c <= m; c++) {
        for (let o = 0; o <= k; o++) {
            if (o + popcount(c) === k) {
                total = (total + dp[idx(m, c, o)]) % MOD;
            }
        }
    }
    return Number((BigInt(total) * fact[m]) % MODn);
};
