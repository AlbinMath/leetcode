var maxDifference = function(s) {
    let freq = Array(26).fill(0);

    // Count character frequencies
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let maxOdd = 0;
    let minEven = Infinity;

    // Find maximum odd frequency and minimum even frequency
    for (const f of freq) {
        if (f === 0) continue;

        if (f % 2 === 1) {
            maxOdd = Math.max(maxOdd, f);
        } else {
            minEven = Math.min(minEven, f);
        }
    }

    return maxOdd - minEven;
};
