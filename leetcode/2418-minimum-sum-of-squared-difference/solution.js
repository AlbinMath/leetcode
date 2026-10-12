
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    const n = nums1.length;
    let k = k1 + k2;
    const diff = new Array(n);

    let maxDiff = 0;

    for (let i = 0; i < n; i++) {
        diff[i] = Math.abs(nums1[i] - nums2[i]);
        maxDiff = Math.max(maxDiff, diff[i]);
    }

    // No difference can be reduced below zero
    if (k >= diff.reduce((sum, d) => sum + d, 0)) {
        return 0;
    }

    // Count the number of differences at each level
    const count = new Array(maxDiff + 1).fill(0);

    for (const d of diff) {
        count[d]++;
    }

    // Reduce the largest differences first
    for (let d = maxDiff; d > 0 && k > 0; d--) {
        const canReduce = Math.min(k, count[d]);

        count[d] -= canReduce;
        count[d - 1] += canReduce;
        k -= canReduce;
    }

    // Calculate the final sum of squared differences
    let result = 0;

    for (let d = 0; d <= maxDiff; d++) {
        result += d * d * count[d];
    }

    return result;
};

