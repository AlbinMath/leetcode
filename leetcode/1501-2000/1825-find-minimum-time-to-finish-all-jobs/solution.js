
/**
 * @param {number[]} jobs
 * @param {number} k
 * @return {number}
 */
var minimumTimeRequired = function(jobs, k) {
    const n = jobs.length;
    const totalMasks = 1 << n;

    // sum[mask] = total time for the jobs selected by mask.
    const sum = new Array(totalMasks).fill(0);

    for (let mask = 1; mask < totalMasks; mask++) {
        const bit = mask & -mask;
        const index = Math.log2(bit);

        sum[mask] = sum[mask ^ bit] + jobs[index];
    }

    // dp[w][mask] = minimum possible maximum workload
    // when assigning jobs in mask to w workers.
    const dp = Array.from(
        { length: k + 1 },
        () => new Array(totalMasks).fill(Infinity)
    );

    dp[0][0] = 0;

    for (let w = 1; w <= k; w++) {
        for (let mask = 0; mask < totalMasks; mask++) {
            // The last worker must receive a non-empty subset
            // of the jobs represented by mask.
            for (
                let sub = mask;
                sub > 0;
                sub = (sub - 1) & mask
            ) {
                const remaining = mask ^ sub;

                if (dp[w - 1][remaining] === Infinity) {
                    continue;
                }

                dp[w][mask] = Math.min(
                    dp[w][mask],
                    Math.max(
                        dp[w - 1][remaining],
                        sum[sub]
                    )
                );
            }
        }
    }

    return dp[k][totalMasks - 1];
};

