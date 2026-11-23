
var modifiedGraphEdges = function (n, edges, source, destination, target) {
    const INF = Number.MAX_SAFE_INTEGER;
    const eid = Array.from({ length: n }, () => new Array(n).fill(-1));
    const cur = edges.map((e) => (e[2] === -1 ? 1 : e[2])); // working weights
    const isVar = edges.map((e) => e[2] === -1);

    edges.forEach(([a, b], i) => {
        eid[a][b] = i;
        eid[b][a] = i;
    });

    const dijkstra = (pass, d0, delta) => {
        const d = new Array(n).fill(INF);
        const done = new Array(n).fill(false);
        d[source] = 0;
        for (let iter = 0; iter < n; iter++) {
            let u = -1;
            for (let i = 0; i < n; i++) {
                if (!done[i] && (u === -1 || d[i] < d[u])) u = i;
            }
            if (u === -1 || d[u] === INF) break;
            done[u] = true;
            for (let v = 0; v < n; v++) {
                const i = eid[u][v];
                if (i === -1) continue;
                if (pass === 1 && isVar[i]) {
                    const need = delta + d0[v] - d[u];
                    if (need > cur[i]) cur[i] = need;
                }
                if (d[u] + cur[i] < d[v]) d[v] = d[u] + cur[i];
            }
        }
        return d;
    };

    const d0 = dijkstra(0, null, 0);
    if (d0[destination] > target) return [];

    const delta = target - d0[destination];
    const d1 = dijkstra(1, d0, delta);
    if (d1[destination] !== target) return [];

    return edges.map(([a, b], i) => [a, b, cur[i]]);
};
