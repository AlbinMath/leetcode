
var splitArray = function(nums) {
    const n = nums.length;

    // 1. Sieve of Eratosthenes to mark prime indices up to n - 1
    const isPrime = new Uint8Array(n).fill(1);
    isPrime[0] = 0;
    if (n > 1) isPrime[1] = 0;

    for (let i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Accumulate sum(A) - sum(B)
    let diff = 0;
    for (let i = 0; i < n; i++) {
        if (isPrime[i]) {
            diff += nums[i];
        } else {
            diff -= nums[i];
        }
    }

    return Math.abs(diff);
};
