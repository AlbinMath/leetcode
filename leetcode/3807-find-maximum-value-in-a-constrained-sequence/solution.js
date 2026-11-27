var findMaxVal = function(n, restrictions, diff) {
    const limit = new Array(n).fill(Infinity);

    limit[0] = 0;

    for (const [idx, maxVal] of restrictions) {
        limit[idx] = Math.min(limit[idx], maxVal);
    }

    for (let i = 1; i < n; i++) {
        limit[i] = Math.min(
            limit[i],
            limit[i - 1] + diff[i - 1]
        );
    }

    for (let i = n - 2; i >= 0; i--) {
        limit[i] = Math.min(
            limit[i],
            limit[i + 1] + diff[i]
        );
    }

    let ans = 0;

    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, limit[i]);
    }

    return ans;
};
