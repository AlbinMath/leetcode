
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    const n = nums.length;
    const totalMasks = 1 << n;
    const memo = new Array(totalMasks).fill(-1);

    function gcd(a, b) {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    function countBits(mask) {
        let count = 0;

        while (mask > 0) {
            mask &= mask - 1;
            count++;
        }

        return count;
    }

    function dp(mask) {
        if (mask === totalMasks - 1) {
            return 0;
        }

        if (memo[mask] !== -1) {
            return memo[mask];
        }

        const operation = countBits(mask) / 2 + 1;
        let best = 0;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            for (let j = i + 1; j < n; j++) {
                if (mask & (1 << j)) continue;

                const nextMask =
                    mask | (1 << i) | (1 << j);

                const score =
                    operation * gcd(nums[i], nums[j]) +
                    dp(nextMask);

                best = Math.max(best, score);
            }
        }

        memo[mask] = best;
        return best;
    }

    return dp(0);
};

