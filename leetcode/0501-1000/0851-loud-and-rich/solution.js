/**
 * @param {number[][]} richer
 * @param {number[]} quiet
 * @return {number[]}
 */
var loudAndRich = function (richer, quiet) {
    const n = quiet.length;
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Array(n).fill(0);

    for (const [a, b] of richer) {
        adj[a].push(b);
        indeg[b]++;
    }

    const ans = Array.from({ length: n }, (_, i) => i);
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        for (const v of adj[u]) {
            if (quiet[ans[u]] < quiet[ans[v]]) ans[v] = ans[u];
            if (--indeg[v] === 0) queue.push(v);
        }
    }
    return ans;
};
