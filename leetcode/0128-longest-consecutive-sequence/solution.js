
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let longest = 0;

    for (const num of numSet) {
        // Start only at the beginning of a sequence
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let length = 1;

            while (numSet.has(currentNum + 1)) {
                currentNum++;
                length++;
            }

            longest = Math.max(longest, length);
        }
    }

    return longest;
};

