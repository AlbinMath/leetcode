
var minTimeToReach = function (moveTime) {
    const n = moveTime.length, m = moveTime[0].length;
    const V = n * m;
    const SHIFT = 1048576; // 2^20 > 562500
    const dist = new Float64Array(V).fill(Infinity);
    dist[0] = 0;

    // Min-heap of encoded keys: time * SHIFT + index
    const heap = new Float64Array(4 * V + 4);
    let size = 0;
    const push = (key) => {
        let i = size++;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= key) break;
            heap[i] = heap[p];
            i = p;
        }
        heap[i] = key;
    };
    const pop = () => {
        const top = heap[0];
        const last = heap[--size];
        let i = 0;
        while (true) {
            let l = 2 * i + 1;
            if (l >= size) break;
            if (l + 1 < size && heap[l + 1] < heap[l]) l++;
            if (heap[l] >= last) break;
            heap[i] = heap[l];
            i = l;
        }
        heap[i] = last;
        return top;
    };

    const dr = [1, -1, 0, 0], dc = [0, 0, 1, -1];
    push(0);

    while (size > 0) {
        const key = pop();
        const u = key % SHIFT;
        const t = (key - u) / SHIFT;
        if (t > dist[u]) continue;
        if (u === V - 1) return t;

        const r = (u / m) | 0, c = u % m;
        const cost = ((r + c) & 1) === 0 ? 1 : 2;
        for (let d = 0; d < 4; d++) {
            const nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            const nt = Math.max(t, moveTime[nr][nc]) + cost;
            const ni = nr * m + nc;
            if (nt < dist[ni]) {
                dist[ni] = nt;
                push(nt * SHIFT + ni);
            }
        }
    }
    return dist[V - 1];
};
