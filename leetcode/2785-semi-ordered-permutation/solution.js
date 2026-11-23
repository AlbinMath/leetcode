var semiOrderedPermutation = function(nums) {
    const n = nums.length;
    const idx1 = nums.indexOf(1);
    const idxN = nums.indexOf(n);

    const swaps = idx1 + (n - 1 - idxN);
    return idx1 > idxN ? swaps - 1 : swaps;
};
