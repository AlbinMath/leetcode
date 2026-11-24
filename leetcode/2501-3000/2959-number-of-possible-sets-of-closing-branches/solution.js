
var numberOfSets = function (n, maxDistance, roads) {
    const INF = 1e9;

    // Base matrix with the cheapest road between each pair
    const base = Array.from({ length: n }, () => new Array(n).fill(INF));
    for (let i = 0; i < n; i++) base[i][i] = 0;
    for (const [u, v, w] of roads) {
        if (w < base[u][v]) {
            base[u][v] = w;
            base[v][u] = w;
        }
    }

    let count = 0;
    for (let mask = 0; mask < (1 << n); mask++) {
        // Copy distances among active nodes only
        const d = base.map((row) => row.slice());

        // Floyd-Warshall, using only active intermediate nodes
        for (let k = 0; k < n; k++) {
            if (!(mask >> k & 1)) continue;
            for (let i = 0; i < n; i++) {
                if (!(mask >> i & 1)) continue;
                for (let j = 0; j < n; j++) {
                    if (!(mask >> j & 1)) continue;
                    if (d[i][k] + d[k][j] < d[i][j]) {
                        d[i][j] = d[i][k] + d[k][j];
                    }
                }
            }
        }

        let ok = true;
        for (let i = 0; i < n && ok; i++) {
            if (!(mask >> i & 1)) continue;
            for (let j = i + 1; j < n; j++) {
                if (!(mask >> j & 1)) continue;
                if (d[i][j] > maxDistance) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) count++;
    }
    return count;
};
