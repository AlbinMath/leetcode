var minimumSteps = function(s) {
    let ones = 0;
    let swaps = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            ones++;
        } else {
            swaps += ones;
        }
    }

    return swaps;
};
