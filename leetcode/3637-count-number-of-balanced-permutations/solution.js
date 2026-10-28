
var countBalancedPermutations = function(num) {
    const MOD = 1000000007n;
    const velunexorai = num;
    const n = velunexorai.length;

    const cnt = Array(10).fill(0);
    let total = 0;

    for (const ch of velunexorai) {
        const d = Number(ch);
        cnt[d]++;
        total += d;
    }

    if (total % 2 !== 0) return 0;

    const target = total / 2;
    const even = Math.ceil(n / 2);
    const odd = Math.floor(n / 2);

    const fact = Array(n + 1).fill(1n);
    const invFact = Array(n + 1).fill(1n);

    function modPow(a, b) {
        let res = 1n;
        while (b > 0n) {
            if (b & 1n) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1n;
        }
        return res;
    }

    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    let dp = Array.from(
        { length: even + 1 },
        () => Array(target + 1).fill(0n)
    );
    dp[0][0] = 1n;

    let processed = 0;

    for (let d = 0; d <= 9; d++) {
        const c = cnt[d];
        if (c === 0) continue;

        const next = Array.from(
            { length: even + 1 },
            () => Array(target + 1).fill(0n)
        );

        for (let used = 0; used <= Math.min(processed, even); used++) {
            for (let sum = 0; sum <= target; sum++) {
                const cur = dp[used][sum];
                if (cur === 0n) continue;

                for (let take = 0; take <= c; take++) {
                    const newUsed = used + take;
                    const newSum = sum + take * d;

                    if (newUsed > even || newSum > target) break;

                    const ways = cur * invFact[take] % MOD *
                        invFact[c - take] % MOD;

                    next[newUsed][newSum] =
                        (next[newUsed][newSum] + ways) % MOD;
                }
            }
        }

        dp = next;
        processed += c;
    }

    return Number(
        dp[even][target] * fact[even] % MOD * fact[odd] % MOD
    );
};

