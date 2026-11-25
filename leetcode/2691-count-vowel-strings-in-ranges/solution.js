
var vowelStrings = function(words, queries) {
    const n = words.length;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        let word = words[i];

        let first = word[0];
        let last = word[word.length - 1];

        let isValid = vowels.has(first) && vowels.has(last);

        prefix[i + 1] = prefix[i] + (isValid ? 1 : 0);
    }

    let result = [];

    for (let [l, r] of queries) {
        result.push(prefix[r + 1] - prefix[l]);
    }

    return result;
};

