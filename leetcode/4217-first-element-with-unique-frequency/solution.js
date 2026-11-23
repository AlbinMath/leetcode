
var firstUniqueFreq = function(nums) {
    const freq = new Map();

    // Step 1: Count frequency of each number
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Step 2: Count how many numbers have each frequency
    const freqCount = new Map();

    for (let count of freq.values()) {
        freqCount.set(count, (freqCount.get(count) || 0) + 1);
    }

    // Step 3: Find the first number with unique frequency
    for (let num of nums) {
        const count = freq.get(num);

        if (freqCount.get(count) === 1) {
            return num;
        }
    }

    return -1;
};

