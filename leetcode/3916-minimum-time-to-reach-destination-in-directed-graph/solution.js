
var minTime = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, s, e] of edges) adj[u].push([v, s, e]);

    // Min-heap of [time, node]
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
        const [t, u] = pop();
        if (t > dist[u]) continue;
        if (u === n - 1) return t;
        for (const [v, s, e] of adj[u]) {
            if (t > e) continue;
            const nt = Math.max(t, s) + 1;
            if (nt < dist[v]) {
                dist[v] = nt;
                push([nt, v]);
            }
        }
    }
    return -1;
};
