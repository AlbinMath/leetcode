var findValidPair = function(s) {
    let freq = Array(10).fill(0);

    // Count frequency of each digit
    for (const ch of s) {
        freq[Number(ch)]++;
    }

    // Traverse adjacent pairs from left to right
    for (let i = 0; i < s.length - 1; i++) {
        let a = Number(s[i]);
        let b = Number(s[i + 1]);

        if (a !== b && freq[a] === a && freq[b] === b) {
            return s[i] + s[i + 1];
        }
    }

    return "";
};
