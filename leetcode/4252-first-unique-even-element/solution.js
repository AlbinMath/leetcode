
var firstUniqueEven = function(nums) {
    const freq = new Map();

    // Step 1: Count frequency of each number
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Step 2: Find the first unique even number
    for (let num of nums) {
        if (num % 2 === 0 && freq.get(num) === 1) {
            return num;
        }
    }

    return -1;
};

