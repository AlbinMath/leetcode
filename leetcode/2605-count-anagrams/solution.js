var countAnagrams = function(s) {
    const MOD = 1000000007n;
    const n = s.length;

    const fact = Array(n + 1).fill(1n);
    const invFact = Array(n + 1).fill(1n);

    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    function modPow(a, b) {
        let result = 1n;

        while (b > 0n) {
            if (b % 2n === 1n) {
                result = result * a % MOD;
            }
            a = a * a % MOD;
            b /= 2n;
        }

        return result;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);

    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    let answer = 1n;

    for (const word of s.split(' ')) {
        const freq = Array(26).fill(0);

        for (const ch of word) {
            freq[ch.charCodeAt(0) - 97]++;
        }

        let ways = fact[word.length];

        for (const count of freq) {
            ways = ways * invFact[count] % MOD;
        }

        answer = answer * ways % MOD;
    }

    return Number(answer);
};
