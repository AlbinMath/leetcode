
var kthDistinct = function(arr, k) {
    const freq = new Map();

    // Count the frequency of each string.
    for (const str of arr) {
        freq.set(str, (freq.get(str) || 0) + 1);
    }

    // Find the kth distinct string in original order.
    for (const str of arr) {
        if (freq.get(str) === 1) {
            k--;

            if (k === 0) {
                return str;
            }
        }
    }

    return "";
};

