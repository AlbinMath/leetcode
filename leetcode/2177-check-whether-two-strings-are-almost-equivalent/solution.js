
var checkAlmostEquivalent = function(word1, word2) {
    const freq = new Array(26).fill(0);

    for (const ch of word1) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    for (const ch of word2) {
        freq[ch.charCodeAt(0) - 97]--;
    }

    for (const count of freq) {
        if (Math.abs(count) > 3) {
            return false;
        }
    }

    return true;
};

