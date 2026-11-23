
var largestPrime = function(n) {
    if (n < 2) return 0;

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

    // 2. Sum consecutive primes starting from 2 while sum <= n
    let sum = 0;
    let ans = 0;

    for (let p = 2; p <= n; p++) {
        if (isPrime[p]) {
            sum += p;
            if (sum > n) break;
            if (isPrime[sum]) {
                ans = sum;
            }
        }
    }

    return ans;
};
