
var maxSubstringLength = function(s, k) {
    if (k === 0) return true;

    const n = s.length;

    const first = new Array(26).fill(n);
    const last = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;

        first[c] = Math.min(first[c], i);
        last[c] = i;
    }

    const intervals = [];
    for (let c = 0; c < 26; c++) {
        if (last[c] === -1) continue;

        const start = first[c];
        let end = last[c];
        let valid = true;
        for (let i = start; i <= end; i++) {
            const x = s.charCodeAt(i) - 97;

            if (first[x] < start) {
                valid = false;
                break;
            }

            end = Math.max(end, last[x]);
        }
        if (valid && !(start === 0 && end === n - 1)) {
            intervals.push([start, end]);
        }
    }
    intervals.sort((a, b) => a[1] - b[1]);
    let count = 0;
    let previousEnd = -1;

    for (const [start, end] of intervals) {
        if (start > previousEnd) {
            count++;
            previousEnd = end;

            if (count >= k) return true;
        }
    }

    return false;
};

