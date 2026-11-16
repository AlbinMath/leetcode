
var longestSubarray = function(nums, k) {
    const n = nums.length;
    let maxVal = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    // 1. Build Smallest Prime Factor (SPF) sieve up to maxVal
    const spf = new Int32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxVal; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    // Helper to extract distinct prime factors of x
    const getPrimeFactors = (x) => {
        const factors = [];
        while (x > 1) {
            const p = spf[x];
            factors.push(p);
            while (x % p === 0) {
                x = Math.floor(x / p);
            }
        }
        return factors;
    };

    // Pre-factorize nums so each element is factorized only once
    const elemFactors = new Array(n);
    for (let i = 0; i < n; i++) {
        elemFactors[i] = getPrimeFactors(nums[i]);
    }

    // 2. Sliding window over nums
    const primeFreq = new Int32Array(maxVal + 1);
    let distinctCount = 0;
    let left = 0;
    let maxLen = 0;

    for (let right = 0; right < n; right++) {
        const rightFactors = elemFactors[right];
        for (let i = 0; i < rightFactors.length; i++) {
            const p = rightFactors[i];
            if (primeFreq[p] === 0) distinctCount++;
            primeFreq[p]++;
        }

        while (distinctCount > k) {
            const leftFactors = elemFactors[left];
            for (let i = 0; i < leftFactors.length; i++) {
                const p = leftFactors[i];
                primeFreq[p]--;
                if (primeFreq[p] === 0) distinctCount--;
            }
            left++;
        }

        const windowLen = right - left + 1;
        if (windowLen > maxLen) {
            maxLen = windowLen;
        }
    }

    return maxLen;
};
