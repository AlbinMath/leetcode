var beautifulPartitions = function(s, k, minLength) {
    const MOD = 1000000007;
    const n = s.length;
    const isPrime = (digit) => {
        return digit === '2' ||
               digit === '3' ||
               digit === '5' ||
               digit === '7';
    };
    if (!isPrime(s[0]) || isPrime(s[n - 1])) {
        return 0;
    }
    if (k * minLength > n) {
        return 0;
    }
    let prev = new Array(n + 1).fill(0);
    prev[0] = 1;
    for (let part = 1; part <= k; part++) {
        let curr = new Array(n + 1).fill(0);
        let ways = 0;
        for (let i = 1; i <= n; i++) {
            let t = i - minLength;
            if (
                t >= 0 &&
                isPrime(s[t]) &&
                (t === 0 || !isPrime(s[t - 1]))
            ) {
                ways = (ways + prev[t]) % MOD;
            }
            if (!isPrime(s[i - 1])) {
                curr[i] = ways;
            }
        }
        prev = curr;
    }
    return prev[n];
};

