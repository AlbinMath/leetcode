var maximumNumberOfStringPairs = function(words) {
    const seen = new Set();
    let pairs = 0;

    for (const word of words) {
        const reversed = word[1] + word[0]; // words[i].length is always 2
        if (seen.has(reversed)) {
            pairs++;
        } else {
            seen.add(word);
        }
    }

    return pairs;
};
