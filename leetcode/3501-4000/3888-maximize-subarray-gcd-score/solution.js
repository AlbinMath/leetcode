/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxGCDScore = function(nums, k) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Precompute the highest power of 2 dividing each nums[i]
    // Using division/modulo avoids 32-bit bitwise truncation since nums[i] <= 10^9
    const pow2 = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        let x = nums[i];
        let p = 1;
        while ((x & 1) === 0) {
            x >>= 1;
            p <<= 1;
        }
        pow2[i] = p;
    }

    let maxScore = 0;

    for (let i = 0; i < n; i++) {
        let g = 0;
        let minPow2 = Infinity;
        let minCount = 0;

        for (let j = i; j < n; j++) {
            g = gcd(g, nums[j]);
            const p = pow2[j];

            if (p < minPow2) {
                minPow2 = p;
                minCount = 1;
            } else if (p === minPow2) {
                minCount++;
            }

            const effectiveGcd = minCount <= k ? g * 2 : g;
            const score = effectiveGcd * (j - i + 1);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
};
