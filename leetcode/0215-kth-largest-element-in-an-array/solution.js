var findKthLargest = function(nums, k) {
    const target = nums.length - k;

    function quickSelect(left, right) {
        const randomIndex =
            left + Math.floor(Math.random() * (right - left + 1));

        const pivot = nums[randomIndex];

        let low = left;
        let mid = left;
        let high = right;

        while (mid <= high) {
            if (nums[mid] < pivot) {
                [nums[low], nums[mid]] = [nums[mid], nums[low]];
                low++;
                mid++;
            } else if (nums[mid] > pivot) {
                [nums[mid], nums[high]] = [nums[high], nums[mid]];
                high--;
            } else {
                mid++;
            }
        }

        if (target < low) {
            return quickSelect(left, low - 1);
        }

        if (target > high) {
            return quickSelect(high + 1, right);
        }

        return nums[target];
    }

    return quickSelect(0, nums.length - 1);
};
