/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    if (n < 4) return [];

    // 1. Sieve of Eratosthenes to find all primes up to n
    const isPrime = new Uint8Array(n + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Collect all prime pairs [x, n - x] where x <= n - x
    const result = [];
    const limit = Math.floor(n / 2);

    for (let x = 2; x <= limit; x++) {
        const y = n - x;
        if (isPrime[x] && isPrime[y]) {
            result.push([x, y]);
        }
    }

    return result;
};
