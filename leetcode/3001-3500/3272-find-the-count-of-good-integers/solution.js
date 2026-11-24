var countGoodIntegers = function(n, k) {
    const fact = Array(n + 1).fill(1);
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
    }

    const seen = new Set();
    const half = Math.ceil(n / 2);
    const start = 10 ** (half - 1);
    const end = 10 ** half;
    let ans = 0;

    for (let first = start; first < end; first++) {
        const left = String(first);
        const palindrome = left +
            left.slice(0, n % 2 ? -1 : undefined).split("").reverse().join("");

        if (BigInt(palindrome) % BigInt(k) !== 0n) continue;

        const freq = Array(10).fill(0);
        for (const digit of palindrome) {
            freq[Number(digit)]++;
        }

        const key = freq.join(",");
        if (seen.has(key)) continue;
        seen.add(key);

        let ways = fact[n];
        for (const count of freq) {
            ways /= fact[count];
        }

        if (freq[0] > 0) {
            let leadingZeroWays = fact[n - 1];
            for (let d = 0; d < 10; d++) {
                const count = freq[d] - (d === 0 ? 1 : 0);
                leadingZeroWays /= fact[count];
            }
            ways -= leadingZeroWays;
        }

        ans += ways;
    }

    return ans;
};
