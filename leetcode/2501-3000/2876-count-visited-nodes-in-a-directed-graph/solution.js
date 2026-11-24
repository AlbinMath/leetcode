/**
 * @param {number[]} edges
 * @return {number[]}
 */
var countVisitedNodes = function (edges) {
    const n = edges.length;
    const indeg = new Int32Array(n);
    for (let i = 0; i < n; i++) indeg[edges[i]]++;

    const order = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) order.push(i);
    let head = 0;
    while (head < order.length) {
        const u = order[head++];
        const v = edges[u];
        if (--indeg[v] === 0) order.push(v);
    }

    const ans = new Array(n).fill(0);
    const done = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0 || done[i]) continue; // tree node or already handled cycle node
        let len = 0, cur = i;
        do {
            done[cur] = 1;
            len++;
            cur = edges[cur];
        } while (cur !== i);
        do {
            ans[cur] = len;
            cur = edges[cur];
        } while (cur !== i);
    }

    for (let k = order.length - 1; k >= 0; k--) {
        const u = order[k];
        ans[u] = ans[edges[u]] + 1;
    }
    return ans;
};
