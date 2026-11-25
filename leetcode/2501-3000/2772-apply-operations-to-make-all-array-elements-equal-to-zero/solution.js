
var checkArray = function(nums, k) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);

    let operations = 0;

    for (let i = 0; i < n; i++) {
        operations += diff[i];

        let current = nums[i] - operations;

        if (current < 0) {
            return false;
        }
        if (current === 0) {
            continue;
        }
        if (i + k > n) {
            return false;
        }
        operations += current;
        diff[i + k] -= current;
    }

    return true;
};

