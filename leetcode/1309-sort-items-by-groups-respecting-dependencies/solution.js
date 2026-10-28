/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function (n, m, group, beforeItems) {
    // give ungrouped items their own unique group
    let g = m;
    for (let i = 0; i < n; i++) if (group[i] === -1) group[i] = g++;

    const itemAdj = Array.from({ length: n }, () => []);
    const itemDeg = new Array(n).fill(0);
    const groupAdj = Array.from({ length: g }, () => []);
    const groupDeg = new Array(g).fill(0);

    for (let i = 0; i < n; i++) {
        for (const b of beforeItems[i]) {
            itemAdj[b].push(i);
            itemDeg[i]++;
            if (group[b] !== group[i]) {
                groupAdj[group[b]].push(group[i]);
                groupDeg[group[i]]++;
            }
        }
    }

    const topo = (size, adj, deg) => {
        const q = [];
        for (let i = 0; i < size; i++) if (deg[i] === 0) q.push(i);
        let head = 0;
        while (head < q.length) {
            const u = q[head++];
            for (const v of adj[u]) if (--deg[v] === 0) q.push(v);
        }
        return q.length === size ? q : null;
    };

    const itemOrder = topo(n, itemAdj, itemDeg);
    if (!itemOrder) return [];
    const groupOrder = topo(g, groupAdj, groupDeg);
    if (!groupOrder) return [];

    const buckets = Array.from({ length: g }, () => []);
    for (const it of itemOrder) buckets[group[it]].push(it);

    const res = [];
    for (const gr of groupOrder) for (const it of buckets[gr]) res.push(it);
    return res;
};
