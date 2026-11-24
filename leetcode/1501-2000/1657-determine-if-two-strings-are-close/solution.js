var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) {
        return false;
    }

    const freq1 = new Map();
    const freq2 = new Map();

    for (const ch of word1) {
        freq1.set(ch, (freq1.get(ch) || 0) + 1);
    }

    for (const ch of word2) {
        freq2.set(ch, (freq2.get(ch) || 0) + 1);
    }

    // Both strings must contain the same characters
    if (freq1.size !== freq2.size) {
        return false;
    }

    for (const ch of freq1.keys()) {
        if (!freq2.has(ch)) {
            return false;
        }
    }

    // Compare sorted character frequencies
    const counts1 = [...freq1.values()].sort((a, b) => a - b);
    const counts2 = [...freq2.values()].sort((a, b) => a - b);

    return counts1.every((count, i) => count === counts2[i]);
};
