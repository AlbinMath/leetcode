var findCommonResponse = function(responses) {
    let freq = new Map();

    // Count each response once per day
    for (const day of responses) {
        let unique = new Set(day);

        for (const word of unique) {
            freq.set(word, (freq.get(word) || 0) + 1);
        }
    }

    let result = "";
    let maxFreq = 0;

    // Find most common response
    for (const [word, count] of freq) {
        if (
            count > maxFreq ||
            (count === maxFreq && word < result)
        ) {
            maxFreq = count;
            result = word;
        }
    }

    return result;
};
