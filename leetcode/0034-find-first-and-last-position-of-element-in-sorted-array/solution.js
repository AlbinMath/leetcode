
var searchRange = function(nums, target) {
    function findBound(isFirst) {
        let left = 0;
        let right = nums.length - 1;
        let result = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                result = mid;

                if (isFirst) {
                    // Continue searching to the left
                    right = mid - 1;
                } else {
                    // Continue searching to the right
                    left = mid + 1;
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    const first = findBound(true);
    const last = findBound(false);

    return [first, last];
};

