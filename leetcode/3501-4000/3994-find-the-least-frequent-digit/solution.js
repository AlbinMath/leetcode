var getLeastFrequentDigit = function(n) {
    let freq = new Array(10).fill(0);

    // Count the frequency of each digit
    for (const digit of String(n)) {
        freq[Number(digit)]++;
    }

    let minFreq = Infinity;
    let result = 0;

    // Find the least frequent digit
    for (let i = 0; i <= 9; i++) {
        if (freq[i] > 0 && freq[i] < minFreq) {
            minFreq = freq[i];
            result = i;
        }
    }

    return result;
};
