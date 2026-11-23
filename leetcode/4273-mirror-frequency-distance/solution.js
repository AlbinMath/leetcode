
var mirrorFrequency = function(s) {
    const freq = new Array(36).fill(0);

    // Count character frequencies
    for (const ch of s) {
        let idx = ch >= 'a'
            ? ch.charCodeAt(0) - 97
            : ch.charCodeAt(0) - 48 + 26;

        freq[idx]++;
    }

    let ans = 0;

    // Calculate mirror frequency differences
    for (let i = 0; i < 36; i++) {
        let mirror = i < 26 ? 25 - i : 61 - i;

        // Count each pair only once
        if (i < mirror) {
            ans += Math.abs(freq[i] - freq[mirror]);
        }
    }

    return ans;
};

