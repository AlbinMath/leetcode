
var canMakeEqual = function(nums, k) {
    const n = nums.length;

    function check(target) {
        let operations = 0;
        for (let i = 0; i < n - 1; i++) {
            if (nums[i] !== target) {
                nums[i] *= -1;
                nums[i + 1] *= -1;
                operations++;
            }
        }
        return nums[n - 1] === target && operations <= k;
    }
    const original = nums.slice();

    if (check(1)) {
        return true;
    }
    for (let i = 0; i < n; i++) {
        nums[i] = original[i];
    }
    return check(-1);
};

