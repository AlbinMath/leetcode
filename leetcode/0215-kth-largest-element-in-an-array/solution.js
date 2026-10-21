
var findKthLargest = function(nums, k) {
    const target = nums.length - k;
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        // Select a random pivot
        const randomIndex =
            left + Math.floor(Math.random() * (right - left + 1));

        const pivot = nums[randomIndex];

        // Move the pivot to the end
        [nums[randomIndex], nums[right]] =
            [nums[right], nums[randomIndex]];

        // Three-way partition:
        // [left, lt - 1] < pivot
        // [lt, i - 1] === pivot
        // [gt + 1, right] > pivot
        let lt = left;
        let i = left;
        let gt = right;

        while (i <= gt) {
            if (nums[i] < pivot) {
                [nums[lt], nums[i]] = [nums[i], nums[lt]];
                lt++;
                i++;
            } else if (nums[i] > pivot) {
                [nums[i], nums[gt]] = [nums[gt], nums[i]];
                gt--;
            } else {
                i++;
            }
        }

        if (target < lt) {
            right = lt - 1;
        } else if (target > gt) {
            left = gt + 1;
        } else {
            return pivot;
        }
    }

    return -1;
};

