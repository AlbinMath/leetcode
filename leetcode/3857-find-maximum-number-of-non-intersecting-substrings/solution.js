
var maxSubstrings = function(word) {
    const n = word.length;

    const nextEnd = new Int32Array(n).fill(-1);
    const nearest = new Int32Array(26).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        if (i + 3 < n) {
            const c = word.charCodeAt(i + 3) - 97;
            nearest[c] = i + 3;
        }

        const c = word.charCodeAt(i) - 97;
        nextEnd[i] = nearest[c];
    }
    let count = 0;
    let earliestEnd = n;

    for (let i = 0; i < n; i++) {
        const end = nextEnd[i];

        if (end !== -1) {
            earliestEnd = Math.min(earliestEnd, end);
        }
        if (i === earliestEnd) {
            count++;
            earliestEnd = n;
        }
    }

    return count;
};

