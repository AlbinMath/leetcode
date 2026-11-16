/**
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var nonSpecialCount = function(l, r) {
    const limit = Math.floor(Math.sqrt(r));
    
    // 1. Sieve of Eratosthenes up to floor(sqrt(r))
    const isPrime = new Uint8Array(limit + 1).fill(1);
    isPrime[0] = 0;
    if (limit >= 1) isPrime[1] = 0;

    for (let i = 2; i * i <= limit; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= limit; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Count special numbers (p^2) in [l, r]
    let specialCount = 0;
    const start = Math.ceil(Math.sqrt(l));

    for (let p = start; p <= limit; p++) {
        if (isPrime[p]) {
            specialCount++;
        }
    }

    // 3. Subtract special numbers from total integers in [l, r]
    return (r - l + 1) - specialCount;
};
