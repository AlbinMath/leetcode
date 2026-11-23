var secondsToRemoveOccurrences = function(s) {
    let zeros = 0;
    let seconds = 0;

    for (const ch of s) {
        if (ch === '0') {
            zeros++;
        } else if (zeros > 0) {
            seconds = Math.max(seconds + 1, zeros);
        }
    }

    return seconds;
};
