
var minCost = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, 2 * w]);
    }

    // Min-heap of [cost, node]
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
    dist[0] = 0;
    push([0, 0]);

    while (heap.length) {
        const [d, u] = pop();
        if (d > dist[u]) continue;
        if (u === n - 1) return d;
        for (const [v, w] of adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                push([nd, v]);
            }
        }
    }
    return -1;
};
