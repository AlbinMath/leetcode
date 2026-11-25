
var maximumSubsequenceCount = function(text, pattern) {
    let countFirst = 0;
    let countSecond = 0;
    let subsequences = 0;

    for (let ch of text) {
        if (ch === pattern[1]) {
            subsequences += countFirst;
            countSecond++;
        }

        if (ch === pattern[0]) {
            countFirst++;
        }
    }
    return subsequences + Math.max(countFirst, countSecond);
};
