
var prefixConnected = function(words, k) {
    const map = new Map();

    // Step 1: Count prefix frequencies
    for (let word of words) {
        if (word.length < k) {
            continue;
        }

        const prefix = word.substring(0, k);

        map.set(prefix, (map.get(prefix) || 0) + 1);
    }

    // Step 2: Count groups with at least 2 words
    let count = 0;

    for (let freq of map.values()) {
        if (freq >= 2) {
            count++;
        }
    }

    return count;
};

