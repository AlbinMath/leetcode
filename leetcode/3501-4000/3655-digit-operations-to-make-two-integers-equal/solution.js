/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var minOperations = function (n, m) {
    const LIMIT = 10000;
    const composite = new Uint8Array(LIMIT);
    composite[0] = 1; // 0 and 1 are not prime
    composite[1] = 1;
    const prime = new Uint8Array(LIMIT).fill(1);
    prime[0] = 0;
    prime[1] = 0;
    for (let i = 2; i * i < LIMIT; i++) {
        if (prime[i]) {
            for (let j = i * i; j < LIMIT; j += i) prime[j] = 0;
        }
    }

    if (prime[n] || prime[m]) return -1;

    const len = String(n).length;
    const lo = len === 1 ? 0 : Math.pow(10, len - 1);

    const dist = new Float64Array(LIMIT).fill(Infinity);
    dist[n] = n;

    // Min-heap of [cost, node] stored as parallel arrays
    const hc = [];
    const hn = [];
    const push = (c, v) => {
        let i = hc.length;
        hc.push(c);
        hn.push(v);
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (hc[p] <= hc[i]) break;
            let t = hc[p]; hc[p] = hc[i]; hc[i] = t;
            t = hn[p]; hn[p] = hn[i]; hn[i] = t;
            i = p;
        }
    };
    const pop = () => {
        const c = hc[0], v = hn[0];
        const lc = hc.pop(), lv = hn.pop();
        const size = hc.length;
        if (size > 0) {
            hc[0] = lc;
            hn[0] = lv;
            let i = 0;
            while (true) {
                const l = 2 * i + 1, r = l + 1;
                let s = i;
                if (l < size && hc[l] < hc[s]) s = l;
                if (r < size && hc[r] < hc[s]) s = r;
                if (s === i) break;
                let t = hc[s]; hc[s] = hc[i]; hc[i] = t;
                t = hn[s]; hn[s] = hn[i]; hn[i] = t;
                i = s;
            }
        }
        return [c, v];
    };

    push(n, n);
    while (hc.length) {
        const [c, u] = pop();
        if (c > dist[u]) continue;
        if (u === m) return c;

        let p = 1;
        for (let k = 0; k < len; k++, p *= 10) {
            const digit = ((u / p) | 0) % 10;
            if (digit < 9) {
                const v = u + p;
                const nc = c + v;
                if (!prime[v] && nc < dist[v]) {
                    dist[v] = nc;
                    push(nc, v);
                }
            }
            if (digit > 0) {
                const v = u - p;
                const nc = c + v;
                if (v >= lo && !prime[v] && nc < dist[v]) {
                    dist[v] = nc;
                    push(nc, v);
                }
            }
        }
    }
    return -1;
};
