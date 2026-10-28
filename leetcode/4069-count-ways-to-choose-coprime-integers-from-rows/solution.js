/**
 * @param {number[][]} mat
 * @return {number}
 */
var countCoprime = function (mat) {
    const MOD = 1000000007n;
    const MAXV = 150;

    // Möbius function via sieve
    const mu = new Array(MAXV + 1).fill(1);
    const isComp = new Array(MAXV + 1).fill(false);
    for (let p = 2; p <= MAXV; p++) {
        if (isComp[p]) continue;
        for (let j = p; j <= MAXV; j += p) {
            if (j > p) isComp[j] = true;
            mu[j] = -mu[j];
        }
        const sq = p * p;
        for (let j = sq; j <= MAXV; j += sq) mu[j] = 0;
    }

    let ans = 0n;
    for (let d = 1; d <= MAXV; d++) {
        if (mu[d] === 0) continue;

        let prod = 1n;
        for (const row of mat) {
            let cnt = 0;
            for (const x of row) if (x % d === 0) cnt++;
            if (cnt === 0) {
                prod = 0n;
                break;
            }
            prod = (prod * BigInt(cnt)) % MOD;
        }

        ans += BigInt(mu[d]) * prod;
        ans %= MOD;
    }

    ans = ((ans % MOD) + MOD) % MOD;
    return Number(ans);
};
