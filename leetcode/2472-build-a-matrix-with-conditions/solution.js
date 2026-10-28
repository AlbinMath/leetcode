/**
 * @param {number} k
 * @param {number[][]} rowConditions
 * @param {number[][]} colConditions
 * @return {number[][]}
 */
var buildMatrix = function (k, rowConditions, colConditions) {
    const topo = (conds) => {
        const adj = Array.from({ length: k + 1 }, () => []);
        const indeg = new Int32Array(k + 1);
        for (const [a, b] of conds) {
            adj[a].push(b);
            indeg[b]++;
        }
        const q = [];
        for (let i = 1; i <= k; i++) if (indeg[i] === 0) q.push(i);
        let head = 0;
        while (head < q.length) {
            const u = q[head++];
            for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
        }
        return q.length === k ? q : null;
    };

    const rows = topo(rowConditions);
    if (!rows) return [];
    const cols = topo(colConditions);
    if (!cols) return [];

    const colPos = new Int32Array(k + 1);
    for (let i = 0; i < k; i++) colPos[cols[i]] = i;

    const mat = Array.from({ length: k }, () => new Array(k).fill(0));
    for (let r = 0; r < k; r++) mat[r][colPos[rows[r]]] = rows[r];
    return mat;
};
