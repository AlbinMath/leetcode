
var sumOfPowers = function(nums, k) {
    const MOD = 1000000007;
    const n = nums.length;

    nums.sort((a, b) => a - b);

    const differences = new Set();

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const diff = nums[j] - nums[i];

            if (diff > 0) {
                differences.add(diff);
            }
        }
    }

    const countAtLeast = function(d) {
        let prev = new Array(n).fill(1);

        for (let len = 2; len <= k; len++) {
            const prefix = new Array(n + 1).fill(0);

            for (let i = 0; i < n; i++) {
                prefix[i + 1] = (prefix[i] + prev[i]) % MOD;
            }

            const curr = new Array(n).fill(0);

            for (let i = 0; i < n; i++) {
                const target = nums[i] - d;

                let left = 0;
                let right = i;

                while (left < right) {
                    const mid = Math.floor((left + right) / 2);

                    if (nums[mid] <= target) {
                        left = mid + 1;
                    } else {
                        right = mid;
                    }
                }

                curr[i] = prefix[left];
            }

            prev = curr;
        }

        let total = 0;

        for (let ways of prev) {
            total = (total + ways) % MOD;
        }

        return total;
    };

    let answer = 0n;
    const bigMOD = BigInt(MOD);

    for (const d of differences) {
        const atLeastD = countAtLeast(d);
        const atLeastNext = countAtLeast(d + 1);

        const exactD = (atLeastD - atLeastNext + MOD) % MOD;

        answer = (
            answer + BigInt(d) * BigInt(exactD)
        ) % bigMOD;
    }

    return Number(answer);
};

