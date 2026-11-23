var validPath = function(n, edges, source, destination) {
    const g = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        g[u].push(v);
        g[v].push(u);
    }

    const seen = new Set([source]);
    const q = [source];

    for (let i = 0; i < q.length; i++) {
        const u = q[i];

        if (u === destination) return true;

        for (const v of g[u]) {
            if (!seen.has(v)) {
                seen.add(v);
                q.push(v);
            }
        }
    }

    return false;
};
