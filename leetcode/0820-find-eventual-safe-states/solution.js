/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function (graph) {
    const n = graph.length;
    const rev = Array.from({ length: n }, () => []);
    const outDeg = new Array(n);

    for (let i = 0; i < n; i++) {
        outDeg[i] = graph[i].length;
        for (const j of graph[i]) rev[j].push(i);
    }

    const queue = [];
    for (let i = 0; i < n; i++) if (outDeg[i] === 0) queue.push(i);

    const safe = new Uint8Array(n);
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        safe[u] = 1;
        for (const p of rev[u]) {
            if (--outDeg[p] === 0) queue.push(p);
        }
    }

    const res = [];
    for (let i = 0; i < n; i++) if (safe[i]) res.push(i);
    return res;
};
