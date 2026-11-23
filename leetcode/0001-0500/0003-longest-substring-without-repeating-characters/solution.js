
var lengthOfLongestSubstring = function(s) {
    const lastSeen = new Map();

    let left = 0;
    let maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        // If the character repeats inside the current window,
        // move left past its previous occurrence
        if (lastSeen.has(char) && lastSeen.get(char) >= left) {
            left = lastSeen.get(char) + 1;
        }

        lastSeen.set(char, right);

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
};

