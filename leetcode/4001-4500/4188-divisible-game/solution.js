
var divisibleGame = function(nums) {
    const n = nums.length;
    const MOD = 1000000007n;

    // 1. Prefix sums of nums to compute negative gaps in O(1)
    const pref = new Float64Array(n + 1);
    let minElem = Infinity;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + nums[i];
        if (nums[i] < minElem) minElem = nums[i];
    }

    // 2. Group indices by each distinct prime factor of nums[i]
    // Always include k = 2 as the baseline candidate
    const primeIndices = new Map();
    primeIndices.set(2, []);

    for (let i = 0; i < n; i++) {
        let x = nums[i];
        if (x % 2 === 0) {
            primeIndices.get(2).push(i);
            while (x % 2 === 0) x /= 2;
        }
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) {
                if (!primeIndices.has(d)) primeIndices.set(d, []);
                primeIndices.get(d).push(i);
                while (x % d === 0) x /= d;
            }
        }
        if (x > 1) {
            if (!primeIndices.has(x)) primeIndices.set(x, []);
            primeIndices.get(x).push(i);
        }
    }

    // Sort candidate primes ascending so ties automatically keep the smallest k
    const primes = Array.from(primeIndices.keys()).sort((a, b) => a - b);

    // Baseline: single smallest element given to Bob with k = 2
    let bestDiff = -minElem;
    let bestK = 2;

    // 3. Run compressed Kadane's algorithm for each candidate prime
    for (const p of primes) {
        const indices = primeIndices.get(p);
        if (indices.length === 0) continue;

        let currentSum = nums[indices[0]];
        let maxSumForP = currentSum;

        for (let idx = 1; idx < indices.length; idx++) {
            const prev = indices[idx - 1];
            const curr = indices[idx];
            // Sum of elements strictly between prev and curr (all subtracted)
            const gapSum = pref[curr] - pref[prev + 1];

            currentSum = Math.max(nums[curr], currentSum - gapSum + nums[curr]);
            if (currentSum > maxSumForP) {
                maxSumForP = currentSum;
            }
        }

        if (maxSumForP > bestDiff) {
            bestDiff = maxSumForP;
            bestK = p;
        }
    }

    const ans = ((BigInt(bestDiff) * BigInt(bestK)) % MOD + MOD) % MOD;
    return Number(ans);
};
