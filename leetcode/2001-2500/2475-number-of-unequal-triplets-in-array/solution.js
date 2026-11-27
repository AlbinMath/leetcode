
var unequalTriplets = function(nums) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    const counts = Array.from(freq.values());

    let result = 0;

    for (let i = 0; i < counts.length; i++) {
        for (let j = i + 1; j < counts.length; j++) {
            for (let k = j + 1; k < counts.length; k++) {
                result += counts[i] * counts[j] * counts[k];
            }
        }
    }

    return result;
};

