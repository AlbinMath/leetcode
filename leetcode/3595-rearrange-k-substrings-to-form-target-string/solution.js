
var isPossibleToRearrange = function(s, t, k) {
    const n = s.length;
    const len = n / k;

    const freq = new Map();

    for (let i = 0; i < n; i += len) {
        const part = s.substring(i, i + len);

        freq.set(part, (freq.get(part) || 0) + 1);
    }

    for (let i = 0; i < n; i += len) {
        const part = t.substring(i, i + len);

        if (!freq.has(part)) {
            return false;
        }

        const count = freq.get(part);

        if (count === 1) {
            freq.delete(part);
        } else {
            freq.set(part, count - 1);
        }
    }

    return true;
};

