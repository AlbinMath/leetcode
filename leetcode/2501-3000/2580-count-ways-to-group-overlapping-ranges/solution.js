
var countWays = function(ranges) {
    const MOD = 1000000007;

    ranges.sort((a, b) => a[0] - b[0]);

    let components = 0;
    let currentEnd = -1;
    for (const [start, end] of ranges) {
        if (start > currentEnd) {
            components++;
            currentEnd = end;
        } else {
            currentEnd = Math.max(currentEnd, end);
        }
    }

    let result = 1;

    for (let i = 0; i < components; i++) {
        result = (result * 2) % MOD;
    }

    return result;
};

