var maxVowels = function(s, k) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let count = 0;

    // Count vowels in the first window
    for (let i = 0; i < k; i++) {
        if (vowels.has(s[i])) {
            count++;
        }
    }

    let maxCount = count;

    // Slide the window
    for (let i = k; i < s.length; i++) {
        if (vowels.has(s[i - k])) {
            count--;
        }

        if (vowels.has(s[i])) {
            count++;
        }

        maxCount = Math.max(maxCount, count);

        // Maximum possible number of vowels found
        if (maxCount === k) {
            return k;
        }
    }

    return maxCount;
};
