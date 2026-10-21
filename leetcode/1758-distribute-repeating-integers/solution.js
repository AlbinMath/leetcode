
/**
 * @param {number[]} nums
 * @param {number[]} quantity
 * @return {boolean}
 */
var canDistribute = function(nums, quantity) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    const counts = [...freq.values()];
    const m = quantity.length;
    const totalMasks = 1 << m;
    const full = totalMasks - 1;

    // Precompute total demand for every customer subset.
    const sum = new Array(totalMasks).fill(0);

    for (let mask = 1; mask < totalMasks; mask++) {
        const bit = mask & -mask;
        const index = Math.log2(bit);

        sum[mask] = sum[mask ^ bit] + quantity[index];
    }

    // dp[mask] = whether this customer subset can be satisfied.
    let dp = new Array(totalMasks).fill(false);
    dp[0] = true;

    for (const count of counts) {
        const next = dp.slice();

        for (let mask = 0; mask < totalMasks; mask++) {
            if (!dp[mask]) continue;

            // Customers not yet assigned.
            const remaining = full ^ mask;

            // Try every non-empty subset of remaining customers.
            for (
                let sub = remaining;
                sub > 0;
                sub = (sub - 1) & remaining
            ) {
                if (sum[sub] <= count) {
                    next[mask | sub] = true;
                }
            }
        }

        dp = next;

        if (dp[full]) return true;
    }

    return dp[full];
};

