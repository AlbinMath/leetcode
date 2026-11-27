var maximumOddBinaryNumber = function(s) {
    let ones = 0;
    let zeros = 0;

    for (let ch of s) {
        if (ch === '1') ones++;
        else zeros++;
    }

    ones--; // Reserve one '1' for the last position

    return '1'.repeat(ones) + '0'.repeat(zeros) + '1';
};
