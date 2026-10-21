
/**
 * @param {number} batchSize
 * @param {number[]} groups
 * @return {number}
 */
var maxHappyGroups = function(batchSize, groups) {
    const counts = new Array(batchSize).fill(0);
    let happy = 0;

    // Count groups by remainder.
    for (const group of groups) {
        const rem = group % batchSize;

        if (rem === 0) {
            happy++;
        } else {
            counts[rem]++;
        }
    }

    const memo = new Map();

    function dfs(remainder) {
        // Encode the remaining group counts and current remainder.
        const key = remainder + "|" + counts.slice(1).join(",");

        if (memo.has(key)) {
            return memo.get(key);
        }

        let best = 0;

        for (let r = 1; r < batchSize; r++) {
            if (counts[r] === 0) continue;

            // Serve one group with remainder r.
            counts[r]--;

            // A group is happy if no donuts are left over
            // before its first customer is served.
            const gain = remainder === 0 ? 1 : 0;

            best = Math.max(
                best,
                gain + dfs((remainder + r) % batchSize)
            );

            // Restore the count for other choices.
            counts[r]++;
        }

        memo.set(key, best);
        return best;
    }

    return happy + dfs(0);
};

