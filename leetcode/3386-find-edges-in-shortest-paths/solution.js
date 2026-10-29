
var findAnswer = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) {
        adj[a].push([b, w]);
        adj[b].push([a, w]);
    }

    const dijkstra = (src) => {
        const heap = [];
        const push = (item) => {
            heap.push(item);
            let i = heap.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (heap[p][0] <= heap[i][0]) break;
                [heap[p], heap[i]] = [heap[i], heap[p]];
                i = p;
            }
        };
        const pop = () => {
            const top = heap[0];
            const last = heap.pop();
            if (heap.length) {
                heap[0] = last;
                let i = 0;
                const len = heap.length;
                while (true) {
                    const l = 2 * i + 1, r = l + 1;
                    let s = i;
                    if (l < len && heap[l][0] < heap[s][0]) s = l;
                    if (r < len && heap[r][0] < heap[s][0]) s = r;
                    if (s === i) break;
                    [heap[s], heap[i]] = [heap[i], heap[s]];
                    i = s;
                }
            }
            return top;
        };

        const dist = new Array(n).fill(Infinity);
        dist[src] = 0;
        push([0, src]);
        while (heap.length) {
            const [t, u] = pop();
            if (t > dist[u]) continue;
            for (const [v, w] of adj[u]) {
                const nt = t + w;
                if (nt < dist[v]) {
                    dist[v] = nt;
                    push([nt, v]);
                }
            }
        }
        return dist;
    };

    const d0 = dijkstra(0);
    const d1 = dijkstra(n - 1);
    const D = d0[n - 1];

    if (D === Infinity) return new Array(edges.length).fill(false);

    return edges.map(([a, b, w]) =>
        d0[a] + w + d1[b] === D || d0[b] + w + d1[a] === D
    );
};
