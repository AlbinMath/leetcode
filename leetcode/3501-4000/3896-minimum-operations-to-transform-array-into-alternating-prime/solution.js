/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    // Smallest prime > 100,000 is 100,003
    const LIMIT = 100005;

    // 1. Sieve of Eratosthenes up to LIMIT
    const isPrime = new Uint8Array(LIMIT + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= LIMIT; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= LIMIT; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Precompute the nearest prime >= x for every x in [1, 100000]
    const nextPrime = new Int32Array(LIMIT + 1);
    let lastPrime = LIMIT;
    for (let x = LIMIT; x >= 1; x--) {
        if (isPrime[x]) lastPrime = x;
        nextPrime[x] = lastPrime;
    }

    // 3. Sum minimum operations across all indices
    let totalOps = 0;

    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];

        if (i % 2 === 0) {
            // Even index: must be prime
            totalOps += nextPrime[val] - val;
        } else {
            // Odd index: must be non-prime
            if (isPrime[val]) {
                totalOps += (val === 2) ? 2 : 1;
            }
        }
    }

    return totalOps;
};
