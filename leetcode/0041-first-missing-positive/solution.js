
var firstMissingPositive = function(nums) {
    const n = nums.length;
    let i = 0;

    // Place each number x at index x - 1
    while (i < n) {
        const correctIndex = nums[i] - 1;

        if (
            nums[i] > 0 &&
            nums[i] <= n &&
            nums[i] !== nums[correctIndex]
        ) {
            // Swap nums[i] into its correct position
            [nums[i], nums[correctIndex]] =
                [nums[correctIndex], nums[i]];
        } else {
            i++;
        }
    }

    // Find the first index that does not contain i + 1
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) {
            return i + 1;
        }
    }

    return n + 1;
};

