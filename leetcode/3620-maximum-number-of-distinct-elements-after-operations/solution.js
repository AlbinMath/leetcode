
var maxDistinctElements = function(nums, k) {
    nums.sort((a, b) => a - b);

    let count = 0;
    let lastUsed = -Infinity;

    for (const num of nums) {
        const smallest = num - k;
        const largest = num + k;
        const chosen = Math.max(smallest, lastUsed + 1);

        if (chosen <= largest) {
            count++;
            lastUsed = chosen;
        }
    }

    return count;
};

