/**
 * @param {string} s
 * @return {number}
 */
var sumOfLargestPrimes = function(s) {
    const isPrime = (num) => {
        if (num < 2) return false;
        if (num === 2 || num === 3) return true;
        if (num % 2 === 0 || num % 3 === 0) return false;

        for (let i = 5; i * i <= num; i += 6) {
            if (num % i === 0 || num % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    const candidates = new Set();
    const n = s.length;

    // 1. Extract all unique substring integers
    for (let i = 0; i < n; i++) {
        let num = 0;
        for (let j = i; j < n; j++) {
            num = num * 10 + (s.charCodeAt(j) - 48);
            candidates.add(num);
        }
    }

    // 2. Filter for prime numbers
    const primes = [];
    for (const num of candidates) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }

    // 3. Sort descending and sum the top 3
    primes.sort((a, b) => b - a);

    let sum = 0;
    const count = Math.min(3, primes.length);
    for (let i = 0; i < count; i++) {
        sum += primes[i];
    }

    return sum;
};
