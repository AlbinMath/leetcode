
var majorityFrequencyGroup = function(s) {
    const freq = new Array(26).fill(0);

    // Step 1: Count frequency of each character
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Step 2: Group characters by their frequency
    const groups = new Map();

    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            if (!groups.has(freq[i])) {
                groups.set(freq[i], []);
            }

            groups.get(freq[i]).push(String.fromCharCode(i + 97));
        }
    }

    // Step 3: Find the majority frequency group
    let result = "";
    let maxSize = 0;
    let maxFreq = 0;

    for (let [frequency, chars] of groups) {
        if (
            chars.length > maxSize ||
            (chars.length === maxSize && frequency > maxFreq)
        ) {
            maxSize = chars.length;
            maxFreq = frequency;
            result = chars.join("");
        }
    }

    return result;
};

