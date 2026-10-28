
var numberOfWays = function(n, x, y) {
    const MOD = 1000000007n;
    const stirling = Array(n + 1).fill(0n);
    stirling[0] = 1n;

    for (let i = 1; i <= n; i++) {
        for (let j = i; j >= 1; j--) {
            stirling[j] =
                (stirling[j - 1] + BigInt(j) * stirling[j]) % MOD;
        }
        stirling[0] = 0n;
    }

    let ans = 0n;
    let falling = 1n;
    let scoreWays = 1n;

    for (let bands = 1; bands <= Math.min(n, x); bands++) {
        falling = falling * BigInt(x - bands + 1) % MOD;
        scoreWays = scoreWays * BigInt(y) % MOD;

        let ways = stirling[bands] * falling % MOD;
        ways = ways * scoreWays % MOD;
        ans = (ans + ways) % MOD;
    }

    return Number(ans);
};

