
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumIncompatibility = function(nums, k) {
    const n = nums.length;
    const groupSize = n / k;

    // A value appearing more than k times cannot be distributed
    // without putting equal values in the same group.
    const freq = new Array(n + 1).fill(0);

    for (const num of nums) {
        freq[num]++;
        if (freq[num] > k) return -1;
    }

    const totalMasks = 1 << n;
    const INF = 1e9;

    // cost[mask] = incompatibility of this valid group,
    // or INF if it is not a valid group of groupSize elements.
    const cost = new Array(totalMasks).fill(INF);

    for (let mask = 1; mask < totalMasks; mask++) {
        if (countBits(mask) !== groupSize) continue;

        let minVal = Infinity;
        let maxVal = -Infinity;
        let seen = 0;
        let valid = true;

        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) === 0) continue;

            const value = nums[i];
            const bit = 1 << value;

            if (seen & bit) {
                valid = false;
                break;
            }

            seen |= bit;
            minVal = Math.min(minVal, value);
            maxVal = Math.max(maxVal, value);
        }

        if (valid) {
            cost[mask] = maxVal - minVal;
        }
    }

    // dp[mask] = minimum cost to distribute the elements in mask.
    const dp = new Array(totalMasks).fill(INF);
    dp[0] = 0;

    for (let mask = 1; mask < totalMasks; mask++) {
        if (countBits(mask) % groupSize !== 0) continue;

        // Fix the first element in the remaining mask.
        // This avoids trying different orders of the same groups.
        const firstBit = mask & -mask;

        for (
            let group = mask;
            group > 0;
            group = (group - 1) & mask
        ) {
            if ((group & firstBit) === 0) continue;
            if (cost[group] === INF) continue;

            const remaining = mask ^ group;

            if (dp[remaining] !== INF) {
                dp[mask] = Math.min(
                    dp[mask],
                    dp[remaining] + cost[group]
                );
            }
        }
    }

    return dp[totalMasks - 1] === INF
        ? -1
        : dp[totalMasks - 1];
};

function countBits(mask) {
    let count = 0;

    while (mask > 0) {
        mask &= mask - 1;
        count++;
    }

    return count;
}

