/**
 * @param {number[]} coins
 * @param {number[][]} edges
 * @return {number}
 */
var collectTheCoins = function (coins, edges) {
    const n = coins.length;
    const adj = Array.from({ length: n }, () => []);
    const deg = new Int32Array(n);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
        deg[a]++;
        deg[b]++;
    }

    const removed = new Uint8Array(n);
    let remaining = n;

    // Stage 1: strip coinless leaves
    let q = [];
    for (let i = 0; i < n; i++) if (deg[i] <= 1 && coins[i] === 0) q.push(i);
    let head = 0;
    while (head < q.length) {
        const u = q[head++];
        if (removed[u]) continue;
        removed[u] = 1;
        remaining--;
        for (const v of adj[u]) {
            if (removed[v]) continue;
            if (--deg[v] <= 1 && coins[v] === 0) q.push(v);
        }
    }

    // Stage 2: peel two layers of leaves
    for (let round = 0; round < 2; round++) {
        const leaves = [];
        for (let i = 0; i < n; i++) if (!removed[i] && deg[i] <= 1) leaves.push(i);
        for (const u of leaves) {
            removed[u] = 1;
            remaining--;
            for (const v of adj[u]) if (!removed[v]) deg[v]--;
        }
    }

    return remaining <= 1 ? 0 : 2 * (remaining - 1);
};
