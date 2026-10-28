var beautifulSubsets = function(nums, k) {
    let count = 0;
    const freq = new Map();

    function backtrack(index) {
        if (index === nums.length) {
            count++;
            return;
        }

        // Skip the current element.
        backtrack(index + 1);

        const num = nums[index];

        // Include it only if num - k and num + k are absent.
        if (!freq.has(num - k) && !freq.has(num + k)) {
            freq.set(num, (freq.get(num) || 0) + 1);

            backtrack(index + 1);

            freq.set(num, freq.get(num) - 1);
            if (freq.get(num) === 0) {
                freq.delete(num);
            }
        }
    }

    backtrack(0);

    return count - 1; // Exclude the empty subset.
};
