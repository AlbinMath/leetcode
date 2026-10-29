
var minTime = function (n, k, m, time, mul) {
    const FULL = (1 << n) - 1;

    // Precompute max time and popcount for every subset
    const maxT = new Float64Array(1 << n);
    const pc = new Uint8Array(1 << n);
    for (let s = 1; s <= FULL; s++) {
        const low = s & -s;
        const idx = 31 - Math.clz32(low);
        const rest = s ^ low;
        maxT[s] = Math.max(maxT[rest], time[idx]);
        pc[s] = pc[rest] + 1;
    }

    const stateId = (mask, side, stage) => (mask * 2 + side) * m + stage;
    const total = (FULL + 1) * 2 * m;
    const dist = new Float64Array(total).fill(Infinity);

    // Min-heap of [cost, state]
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

    const start = stateId(FULL, 0, 0);
    dist[start] = 0;
    push([0, start]);

    while (heap.length) {
        const [cost, id] = pop();
        if (cost > dist[id]) continue;

        const stage = id % m;
        const rest = (id - stage) / m;
        const side = rest % 2;
        const mask = (rest - side) / 2;

        if (mask === 0) return cost;

        if (side === 0) {
            // Send a non-empty group of size <= k from the base
            for (let g = mask; g > 0; g = (g - 1) & mask) {
                if (pc[g] > k) continue;
                const d = maxT[g] * mul[stage];
                const ns = (stage + (Math.floor(d + 1e-9) % m)) % m;
                const nid = stateId(mask ^ g, 1, ns);
                const nc = cost + d;
                if (nc < dist[nid]) {
                    dist[nid] = nc;
                    push([nc, nid]);
                }
            }
        } else {
            // One person at the destination returns
            const atDest = FULL ^ mask;
            for (let r = 0; r < n; r++) {
                if (!((atDest >> r) & 1)) continue;
                const t = time[r] * mul[stage];
                const ns = (stage + (Math.floor(t + 1e-9) % m)) % m;
                const nid = stateId(mask | (1 << r), 0, ns);
                const nc = cost + t;
                if (nc < dist[nid]) {
                    dist[nid] = nc;
                    push([nc, nid]);
                }
            }
        }
    }
    return -1;
};
