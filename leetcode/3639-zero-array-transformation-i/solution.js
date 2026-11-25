var isZeroArray = function(nums, queries) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    for (const [l, r] of queries) {
        diff[l]++;
        diff[r + 1]--;
    }
    let operations = 0;
    for (let i = 0; i < n; i++) {
        operations += diff[i];
        if (operations < nums[i]) {
            return false;
        }
    }
    return true;
};

