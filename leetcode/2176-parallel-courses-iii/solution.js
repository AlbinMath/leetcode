/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number[]} time
 * @return {number}
 */
var minimumTime = function (n, relations, time) {
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    for (const [a, b] of relations) {
        adj[a - 1].push(b - 1);
        indeg[b - 1]++;
    }

    const start = new Int32Array(n);
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let head = 0, ans = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const fin = start[u] + time[u];
        if (fin > ans) ans = fin;
        for (const v of adj[u]) {
            if (fin > start[v]) start[v] = fin;
            if (--indeg[v] === 0) queue.push(v);
        }
    }
    return ans;
};
