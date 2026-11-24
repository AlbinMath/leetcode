
var findCheapestPrice = function (n, flights, src, dst, k) {
    let dist = new Array(n).fill(Infinity);
    dist[src] = 0;

    for (let i = 0; i <= k; i++) {
        const next = dist.slice();
        for (const [u, v, w] of flights) {
            if (dist[u] !== Infinity && dist[u] + w < next[v]) {
                next[v] = dist[u] + w;
            }
        }
        dist = next;
    }

    return dist[dst] === Infinity ? -1 : dist[dst];
};
