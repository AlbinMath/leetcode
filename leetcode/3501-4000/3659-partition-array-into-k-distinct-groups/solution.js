var partitionArray = function(nums, k) {
    let n = nums.length;

    // Check if array can be divided into equal groups
    if (n % k !== 0) {
        return false;
    }

    let freq = new Map();
    let maxFreq = 0;

    // Count frequency of each number
    for (const num of nums) {
        let count = (freq.get(num) || 0) + 1;

        freq.set(num, count);

        maxFreq = Math.max(maxFreq, count);
    }

    // Number of groups
    let groups = n / k;

    return maxFreq <= groups;
};
