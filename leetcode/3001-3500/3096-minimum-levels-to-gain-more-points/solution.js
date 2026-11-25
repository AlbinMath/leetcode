
var minimumLevels = function(possible) {
    const n = possible.length;
    let totalSum = 0;

    for (let num of possible) {
        totalSum += num === 1 ? 1 : -1;
    }
    let prefixSum = 0;
    for (let i = 0; i < n - 1; i++) {
        prefixSum += possible[i] === 1 ? 1 : -1;

        if (2 * prefixSum > totalSum) {
            return i + 1;
        }
    }

    return -1;
};

