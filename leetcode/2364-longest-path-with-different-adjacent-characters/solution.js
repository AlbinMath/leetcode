/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var longestPath = function (parent, s) {
    const n = parent.length;
    const childCnt = new Int32Array(n);
    for (let i = 1; i < n; i++) childCnt[parent[i]]++;

    const top1 = new Int32Array(n);
    const top2 = new Int32Array(n);

    const queue = [];
    for (let i = 0; i < n; i++) if (childCnt[i] === 0) queue.push(i);

    let ans = 1, head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const best = 1 + top1[u];
        const through = 1 + top1[u] + top2[u];
        if (through > ans) ans = through;

        const p = parent[u];
        if (p === -1) continue;

        if (s.charCodeAt(u) !== s.charCodeAt(p)) {
            if (best > top1[p]) {
                top2[p] = top1[p];
                top1[p] = best;
            } else if (best > top2[p]) {
                top2[p] = best;
            }
        }
        if (--childCnt[p] === 0) queue.push(p);
    }
    return ans;
};
