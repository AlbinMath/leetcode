var countVowels = function(word) {
    let total = 0;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const n = word.length;

    for (let i = 0; i < n; i++) {
        if (vowels.has(word[i])) {
            total += (i + 1) * (n - i);
        }
    }

    return total;
};
