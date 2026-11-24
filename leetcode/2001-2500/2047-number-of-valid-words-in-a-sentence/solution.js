
var countValidWords = function(sentence) {
    const tokens = sentence.split(" ");
    let count = 0;

    for (const word of tokens) {
        if (word === "") continue;

        // No digits allowed.
        if (/\d/.test(word)) continue;

        // At most one hyphen, surrounded by lowercase letters.
        if (word.includes("-")) {
            if (!/^[a-z]+(-[a-z]+)?[!.,]?$/.test(word)) {
                continue;
            }
        }

        // Punctuation is allowed only once, at the end.
        if (!/^[a-z-]*[!.,]?$/.test(word)) continue;

        const punctuationCount = (word.match(/[!.,]/g) || []).length;
        const hyphenCount = (word.match(/-/g) || []).length;

        if (punctuationCount > 1 || hyphenCount > 1) continue;

        // A hyphen must have lowercase letters on both sides.
        if (word.includes("-") && !/[a-z]-[a-z]/.test(word)) {
            continue;
        }

        count++;
    }

    return count;
};

