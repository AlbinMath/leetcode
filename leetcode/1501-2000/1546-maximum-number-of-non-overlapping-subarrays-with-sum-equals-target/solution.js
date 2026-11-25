
var maxNonOverlapping = function(nums, target) {
    let count = 0;
    let prefixSum = 0;
    let seen = new Set([0]);

    for (let num of nums) {
        prefixSum += num;

        if (seen.has(prefixSum - target)) {
            count++;

            // Start a fresh search after this subarray
            prefixSum = 0;
            seen = new Set([0]);
        } else {
            seen.add(prefixSum);
        }
    }

    return count;
};

