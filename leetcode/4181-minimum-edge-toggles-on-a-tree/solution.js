/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} start
 * @param {string} target
 * @return {number[]}
 */
var minimumFlips = function (n, edges, start, target) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < n - 1; i++) {
        const [a, b] = edges[i];
        adj[a].push([b, i]);
        adj[b].push([a, i]);
    }

    const diff = new Uint8Array(n);
    for (let i = 0; i < n; i++) diff[i] = start.charCodeAt(i) ^ target.charCodeAt(i);

    const parent = new Int32Array(n).fill(-1);
    const parentEdge = new Int32Array(n).fill(-1);
    const order = [0];
    const seen = new Uint8Array(n);
    seen[0] = 1;
    for (let h = 0; h < order.length; h++) {
        const u = order[h];
        for (const [v, id] of adj[u]) {
            if (!seen[v]) {
                seen[v] = 1;
                parent[v] = u;
                parentEdge[v] = id;
                order.push(v);
            }
        }
    }

    const res = [];
    for (let k = n - 1; k >= 1; k--) {
        const x = order[k];
        if (diff[x]) {
            res.push(parentEdge[x]);
            diff[x] = 0;
            diff[parent[x]] ^= 1;
        }
    }
    if (diff[0]) return [-1];
    res.sort((a, b) => a - b);
    return res;
};
