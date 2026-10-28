
var countKReducibleNumbers = function(s, k) {
    const MOD = 1000000007;
    const n = s.length;

    // steps[i] = operations needed to reduce i to 1
    const steps = Array(n + 1).fill(0);
    for (let i = 2; i <= n; i++) {
        steps[i] = steps[i.toString(2).replace(/0/g, '').length] + 1;
    }

    // If popcount(x) = 1, x needs exactly one operation.
    const good = Array(n + 1).fill(false);
    for (let i = 1; i <= n; i++) {
        good[i] = (i === 1) || (steps[i] + 1 <= k);
    }

    // Binomial coefficients
    const C = Array.from({ length: n + 1 }, () =>
        Array(n + 1).fill(0)
    );
    C[0][0] = 1;

    for (let i = 1; i <= n; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    let ans = 0;

    // Count numbers smaller than s by their number of set bits.
    for (let ones = 1; ones <= n; ones++) {
        if (!good[ones]) continue;

        let remaining = ones;

        for (let i = 0; i < n; i++) {
            if (s[i] === '1') {
                const left = n - i - 1;

                if (remaining >= 0 && remaining <= left) {
                    ans = (ans + C[left][remaining]) % MOD;
                }

                remaining--;
                if (remaining < 0) break;
            }
        }
    }

    // The number n itself is never counted because only branches
    // where a 1 in s is changed to 0 are counted.

    return ans;
};

