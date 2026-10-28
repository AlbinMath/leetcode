var stringCount = function(n) {
    const MOD = 1000000007;

    let dp = Array.from({ length: 2 }, () =>
        Array.from({ length: 3 }, () => Array(2).fill(0))
    );
    dp[0][0][0] = 1;

    for (let i = 0; i < n; i++) {
        const next = Array.from({ length: 2 }, () =>
            Array.from({ length: 3 }, () => Array(2).fill(0))
        );

        for (let l = 0; l < 2; l++) {
            for (let e = 0; e < 3; e++) {
                for (let t = 0; t < 2; t++) {
                    const ways = dp[l][e][t];
                    if (ways === 0) continue;

                    // Choose one of the 23 other letters
                    next[l][e][t] =
                        (next[l][e][t] + ways * 23) % MOD;

                    // Choose 'l'
                    next[1][e][t] =
                        (next[1][e][t] + ways) % MOD;

                    // Choose 'e'
                    next[l][Math.min(2, e + 1)][t] =
                        (next[l][Math.min(2, e + 1)][t] + ways) % MOD;

                    // Choose 't'
                    next[l][e][1] =
                        (next[l][e][1] + ways) % MOD;
                }
            }
        }

        dp = next;
    }

    return dp[1][2][1];
};
