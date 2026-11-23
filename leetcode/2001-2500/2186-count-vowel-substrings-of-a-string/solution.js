
var countVowelSubstrings = function(word) {
    let count = 0;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    for (let i = 0; i < word.length; i++) {
        const seen = new Set();

        for (let j = i; j < word.length; j++) {
            if (!vowels.has(word[j])) {
                break;
            }

            seen.add(word[j]);

            if (seen.size === 5) {
                count++;
            }
        }
    }

    return count;
};

