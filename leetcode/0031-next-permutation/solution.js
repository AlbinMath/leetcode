
var nextPermutation = function(nums) {
    let n = nums.length;
    let i = n - 2;

    // Step 1: Find the first decreasing element from the right
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // Step 2: Find the next larger element from the right and swap
    if (i >= 0) {
        let j = n - 1;

        while (nums[j] <= nums[i]) {
            j--;
        }

        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // Step 3: Reverse the suffix to get the smallest order
    let left = i + 1;
    let right = n - 1;

    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};

