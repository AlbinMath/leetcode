var minDeletion = function(s, k) {
    let freq = {};

    // Count character frequencies
    for (const ch of s) {
        freq[ch] = (freq[ch] || 0) + 1;
    }

    // Get all frequencies and sort ascending
    let arr = Object.values(freq).sort((a, b) => a - b);

    let deletions = 0;
    let remove = arr.length - k;

    // Remove least frequent characters
    for (let i = 0; i < remove; i++) {
        deletions += arr[i];
    }

    return deletions;
};
