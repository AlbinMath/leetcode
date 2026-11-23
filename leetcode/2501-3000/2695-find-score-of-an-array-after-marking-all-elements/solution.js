var findScore = function(nums) {
    const n = nums.length;
    const indices = Array.from({ length: n }, (_, i) => i);

    // Sort indices by value ascending, breaking ties by smaller index
    indices.sort((a, b) => (nums[a] !== nums[b] ? nums[a] - nums[b] : a - b));

    const marked = new Uint8Array(n);
    let score = 0;

    for (const idx of indices) {
        if (!marked[idx]) {
            score += nums[idx];
            marked[idx] = 1;
            if (idx > 0) marked[idx - 1] = 1;
            if (idx + 1 < n) marked[idx + 1] = 1;
        }
    }

    return score;
};
