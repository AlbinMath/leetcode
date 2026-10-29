var minTimeToReach = function (moveTime) {
    const n = moveTime.length, m = moveTime[0].length;
    const V = n * m;
    const dist = new Array(V).fill(Infinity);
    const done = new Array(V).fill(false);
    dist[0] = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let iter = 0; iter < V; iter++) {
        let u = -1;
        for (let i = 0; i < V; i++) {
            if (!done[i] && (u === -1 || dist[i] < dist[u])) u = i;
        }
        if (u === -1 || dist[u] === Infinity) break;
        if (u === V - 1) return dist[u];
        done[u] = true;

        const r = (u / m) | 0, c = u % m;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            const ni = nr * m + nc;
            if (done[ni]) continue;
            const nt = Math.max(dist[u], moveTime[nr][nc]) + 1;
            if (nt < dist[ni]) dist[ni] = nt;
        }
    }
    return dist[V - 1];
};
