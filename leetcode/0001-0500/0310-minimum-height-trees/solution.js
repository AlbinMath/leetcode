/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function (n, edges) {
    if (n === 1) return [0];

    const adj = Array.from({ length: n }, () => []);
    const deg = new Array(n).fill(0);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
        deg[a]++;
        deg[b]++;
    }

    let leaves = [];
    for (let i = 0; i < n; i++) if (deg[i] === 1) leaves.push(i);

    let remaining = n;
    while (remaining > 2) {
        remaining -= leaves.length;
        const next = [];
        for (const leaf of leaves) {
            for (const nb of adj[leaf]) {
                if (--deg[nb] === 1) next.push(nb);
            }
        }
        leaves = next;
    }
    return leaves;
};
