
var minimumTime = function (grid) {
    const m = grid.length, n = grid[0].length;
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;

    // Minimal binary heap storing [time, index]
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
                let l = 2 * i + 1, r = l + 1, s = i;
                if (l < len && heap[l][0] < heap[s][0]) s = l;
                if (r < len && heap[r][0] < heap[s][0]) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    };

    const dist = new Array(m * n).fill(Infinity);
    dist[0] = 0;
    push([0, 0]);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    while (heap.length) {
        const [t, idx] = pop();
        if (t > dist[idx]) continue;
        const r = (idx / n) | 0, c = idx % n;
        if (r === m - 1 && c === n - 1) return t;

        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            let nt = t + 1;
            const need = grid[nr][nc];
            if (nt < need) {
                nt = need + ((need - nt) % 2);
            }
            const ni = nr * n + nc;
            if (nt < dist[ni]) {
                dist[ni] = nt;
                push([nt, ni]);
            }
        }
    }
    return -1;
};
