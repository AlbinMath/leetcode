
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumXORSum = function(nums1, nums2) {
    const n = nums1.length;
    const totalMasks = 1 << n;
    const dp = new Array(totalMasks).fill(Infinity);

    dp[0] = 0;

    for (let mask = 0; mask < totalMasks; mask++) {
        if (dp[mask] === Infinity) continue;

        // Number of selected elements tells us the next index in nums1.
        const i = countBits(mask);

        if (i === n) continue;

        for (let j = 0; j < n; j++) {
            // Skip elements of nums2 that have already been used.
            if (mask & (1 << j)) continue;

            const nextMask = mask | (1 << j);
            const cost = nums1[i] ^ nums2[j];

            dp[nextMask] = Math.min(
                dp[nextMask],
                dp[mask] + cost
            );
        }
    }

    return dp[totalMasks - 1];

    function countBits(mask) {
        let count = 0;

        while (mask > 0) {
            mask &= mask - 1;
            count++;
        }

        return count;
    }
};

