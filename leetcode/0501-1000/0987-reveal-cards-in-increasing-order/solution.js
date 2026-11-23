/**
 * @param {number[]} deck
 * @return {number[]}
 */
var deckRevealedIncreasing = function (deck) {
    const n = deck.length;
    const sorted = [...deck].sort((a, b) => a - b);
    const res = new Array(n);

    const q = [];
    for (let i = 0; i < n; i++) q.push(i);
    let head = 0;

    for (let c = 0; c < n; c++) {
        const idx = q[head++];
        res[idx] = sorted[c];
        if (head < q.length) {
            q.push(q[head++]); // move next top to the bottom
        }
    }
    return res;
};
