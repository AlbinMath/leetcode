
var shiftDistance = function(s, t, nextCost, previousCost) {
    const n = s.length;
    const nextPrefix = new Array(53).fill(0);
    const prevPrefix = new Array(53).fill(0);

    for (let i = 0; i < 52; i++) {
        nextPrefix[i + 1] = nextPrefix[i] + nextCost[i % 26];
        prevPrefix[i + 1] = prevPrefix[i] + previousCost[i % 26];
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const start = s.charCodeAt(i) - 97;
        const end = t.charCodeAt(i) - 97;
        const forward = (end - start + 26) % 26;
        const next = nextPrefix[start + forward] - nextPrefix[start];
        const backward = (start - end + 26) % 26;
        const prev = prevPrefix[start + 1 + 26] -
                     prevPrefix[start + 1 + 26 - backward];

        ans += Math.min(next, prev);
    }

    return ans;
};

