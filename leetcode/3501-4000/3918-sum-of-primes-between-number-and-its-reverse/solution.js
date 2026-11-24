
var sumOfPrimesInRange = function(n) {
    // 1. Reverse the digits of n
    let r = 0;
    let temp = n;
    while (temp > 0) {
        r = r * 10 + (temp % 10);
        temp = Math.floor(temp / 10);
    }

    // 2. Helper to check if a number is prime
    const isPrime = (x) => {
        if (x < 2) return false;
        if (x === 2 || x === 3) return true;
        if (x % 2 === 0 || x % 3 === 0) return false;

        for (let i = 5; i * i <= x; i += 6) {
            if (x % i === 0 || x % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    // 3. Sum all primes in [min(n, r), max(n, r)]
    const low = Math.min(n, r);
    const high = Math.max(n, r);
    let sum = 0;

    for (let x = low; x <= high; x++) {
        if (isPrime(x)) {
            sum += x;
        }
    }

    return sum;
};
