
var countValidPrefixes = function(s) {
    let zeros = 0;
    let ones = 0;
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '0') {
            zeros++;
        } else {
            ones++;
        }

        if (Math.abs(zeros - ones) <= 1) {
            count++;
        }
    }

    return count;
};

