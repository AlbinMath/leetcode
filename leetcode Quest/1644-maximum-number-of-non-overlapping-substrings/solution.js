/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
    const n = s.length;

    // First and last occurrence of each character
    const first = Array(26).fill(n);
    const last = Array(26).fill(-1);

    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        first[c] = Math.min(first[c], i);
        last[c] = i;
    }

    // Find the smallest valid interval starting at index l
    function getInterval(l) {
        let r = last[s.charCodeAt(l) - 97];

        for (let i = l; i <= r; i++) {
            const c = s.charCodeAt(i) - 97;

            // This character appeared before l, so this interval is invalid
            if (first[c] < l) {
                return null;
            }

            // Extend interval to include all occurrences of this character
            r = Math.max(r, last[c]);
        }

        return [l, r];
    }

    const intervals = [];

    // Only the first occurrence of a character can start a valid interval
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;

        if (first[c] === i) {
            const interval = getInterval(i);

            if (interval !== null) {
                intervals.push(interval);
            }
        }
    }

    // Greedily choose the interval with the earliest ending position
    intervals.sort((a, b) => a[1] - b[1]);

    const result = [];
    let prevEnd = -1;

    for (const [l, r] of intervals) {
        if (l > prevEnd) {
            result.push(s.slice(l, r + 1));
            prevEnd = r;
        }
    }

    return result;
};
