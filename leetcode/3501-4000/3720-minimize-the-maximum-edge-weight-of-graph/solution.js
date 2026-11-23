
var minMaxWeight = function (n, edges, threshold) {
    // Reversed adjacency: for edge A -> B, store B -> A
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) adj[b].push([a, w]);

    // Min-heap of [bottleneck, node]
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

    const best = new Array(n).fill(Infinity);
    best[0] = 0;
    push([0, 0]);

    while (heap.length) {
        const [b, u] = pop();
        if (b > best[u]) continue;
        for (const [v, w] of adj[u]) {
            const nb = Math.max(b, w);
            if (nb < best[v]) {
                best[v] = nb;
                push([nb, v]);
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (best[i] === Infinity) return -1;
        if (best[i] > ans) ans = best[i];
    }
    return ans;
};
