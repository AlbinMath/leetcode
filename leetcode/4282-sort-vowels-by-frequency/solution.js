
var sortVowels = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const freq = new Map();

    // Count vowel frequencies
    for (const ch of s) {
        if (vowels.has(ch)) {
            freq.set(ch, (freq.get(ch) || 0) + 1);
        }
    }

    // Sort vowels by frequency (descending)
    // Stable tie-breaking: first occurrence in original string
    const sorted = [...freq.keys()].sort((a, b) => {
        return freq.get(b) - freq.get(a);
    });

    // Build sorted vowel sequence
    let vowelString = '';

    for (const ch of sorted) {
        vowelString += ch.repeat(freq.get(ch));
    }

    // Replace only vowel positions
    let index = 0;
    const result = [];

    for (const ch of s) {
        if (vowels.has(ch)) {
            result.push(vowelString[index++]);
        } else {
            result.push(ch);
        }
    }

    return result.join('');
};

