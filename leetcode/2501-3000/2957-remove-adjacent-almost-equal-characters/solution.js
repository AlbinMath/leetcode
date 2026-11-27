var removeAlmostEqualCharacters = function(word) {
    let count = 0;

    for (let i = 0; i < word.length - 1; i++) {
        let diff = Math.abs(
            word.charCodeAt(i) - word.charCodeAt(i + 1)
        );

        if (diff <= 1) {
            count++;
            i++;
        }
    }

    return count;
};
