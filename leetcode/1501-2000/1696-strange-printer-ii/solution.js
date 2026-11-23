/**
 * @param {number[][]} targetGrid
 * @return {boolean}
 */
var isPrintable = function (targetGrid) {
    const m = targetGrid.length, n = targetGrid[0].length;
    const C = 61;
    const top = new Array(C).fill(Infinity);
    const bot = new Array(C).fill(-1);
    const left = new Array(C).fill(Infinity);
    const right = new Array(C).fill(-1);
    const present = new Array(C).fill(false);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = targetGrid[i][j];
            present[c] = true;
            if (i < top[c]) top[c] = i;
            if (i > bot[c]) bot[c] = i;
            if (j < left[c]) left[c] = j;
            if (j > right[c]) right[c] = j;
        }
    }

    const adj = Array.from({ length: C }, () => new Set());
    const indeg = new Array(C).fill(0);

    for (let c = 1; c < C; c++) {
        if (!present[c]) continue;
        for (let i = top[c]; i <= bot[c]; i++) {
            for (let j = left[c]; j <= right[c]; j++) {
                const d = targetGrid[i][j];
                if (d !== c && !adj[c].has(d)) {
                    adj[c].add(d);
                    indeg[d]++;
                }
            }
        }
    }

    const q = [];
    let total = 0;
    for (let c = 1; c < C; c++) {
        if (!present[c]) continue;
        total++;
        if (indeg[c] === 0) q.push(c);
    }

    let head = 0;
    while (head < q.length) {
        const u = q[head++];
        for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
    }
    return q.length === total;
};
