
var minimumCost = function (start, target, specialRoads) {
    const pts = [start, target];
    const index = new Map();
    const key = (x, y) => x * 100001 + y;
    const getId = (x, y) => {
        const k = key(x, y);
        if (!index.has(k)) {
            index.set(k, pts.length);
            pts.push([x, y]);
        }
        return index.get(k);
    };

    // Reserve ids for start (0) and target (1)
    index.set(key(start[0], start[1]), 0);
    index.set(key(target[0], target[1]), 1);

    const special = []; // [fromId, toId, cost]
    for (const [x1, y1, x2, y2, c] of specialRoads) {
        special.push([getId(x1, y1), getId(x2, y2), c]);
    }

    const V = pts.length;
    const out = Array.from({ length: V }, () => []);
    for (const [a, b, c] of special) out[a].push([b, c]);

    const dist = new Array(V).fill(Infinity);
    const done = new Array(V).fill(false);
    dist[0] = 0;

    for (let iter = 0; iter < V; iter++) {
        let u = -1;
        for (let i = 0; i < V; i++) {
            if (!done[i] && (u === -1 || dist[i] < dist[u])) u = i;
        }
        if (u === -1 || dist[u] === Infinity) break;
        done[u] = true;

        const [ux, uy] = pts[u];
        // Free movement to every other point
        for (let v = 0; v < V; v++) {
            if (done[v]) continue;
            const d = dist[u] + Math.abs(pts[v][0] - ux) + Math.abs(pts[v][1] - uy);
            if (d < dist[v]) dist[v] = d;
        }
        // Special roads leaving u
        for (const [v, c] of out[u]) {
            if (!done[v] && dist[u] + c < dist[v]) dist[v] = dist[u] + c;
        }
    }

    return dist[1];
};
