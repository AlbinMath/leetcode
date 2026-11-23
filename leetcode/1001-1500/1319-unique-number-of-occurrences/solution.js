var uniqueOccurrences = function(arr) {
    const freq = new Map();

    // Count occurrences of each number
    for (const num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Store occurrence counts in a Set
    const counts = new Set(freq.values());

    // If sizes differ, some counts are repeated
    return counts.size === freq.size;
};
