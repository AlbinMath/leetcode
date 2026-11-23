
var checkPrimeFrequency = function(nums) {
    const isPrime = (n) => {
        if (n < 2) return false;
        for (let i = 2; i * i <= n; i++) {
            if (n % i === 0) return false;
        }
        return true;
    };

    // 1. Count frequencies (0 <= nums[i] <= 100)
    const freq = new Uint8Array(101);
    for (const num of nums) {
        freq[num]++;
    }

    // 2. Check if any frequency is prime
    for (let i = 0; i <= 100; i++) {
        if (freq[i] > 1 && isPrime(freq[i])) {
            return true;
        }
    }

    return false;
};
