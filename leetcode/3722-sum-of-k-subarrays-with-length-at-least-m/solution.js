var maxSum = function(nums, k, m) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const NEG_INF = -Infinity;
    let prev = new Array(n + 1).fill(0);
    for (let j = 1; j <= k; j++) {
        const curr = new Array(n + 1).fill(NEG_INF);
        let best = NEG_INF;
        for (let i = 1; i <= n; i++) {
            const p = i - m;
            if (p >= 0 && prev[p] !== NEG_INF) {
                best = Math.max(
                    best,
                    prev[p] - prefix[p]
                );
            }
            curr[i] = curr[i - 1];
            if (best !== NEG_INF) {
                curr[i] = Math.max(
                    curr[i],
                    prefix[i] + best
                );
            }
        }
        prev = curr;
    }
    return prev[n];
};

