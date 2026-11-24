/**
 * @param {number[]} favorite
 * @return {number}
 */
var maximumInvitations = function (favorite) {
    const n = favorite.length;
    const indeg = new Int32Array(n);
    for (let i = 0; i < n; i++) indeg[favorite[i]]++;

    const depth = new Int32Array(n); // longest chain ending at node (excluding itself)
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    const removed = new Uint8Array(n);
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        removed[u] = 1;
        const v = favorite[u];
        if (depth[u] + 1 > depth[v]) depth[v] = depth[u] + 1;
        if (--indeg[v] === 0) queue.push(v);
    }

    let maxCycle = 0, sum2 = 0;
    const seen = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (removed[i] || seen[i]) continue;
        let len = 0, cur = i;
        while (!seen[cur]) {
            seen[cur] = 1;
            len++;
            cur = favorite[cur];
        }
        if (len === 2) {
            const a = i, b = favorite[i];
            sum2 += 2 + depth[a] + depth[b];
        } else if (len > maxCycle) {
            maxCycle = len;
        }
    }
    return Math.max(maxCycle, sum2);
};
