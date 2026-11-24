/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
    const n = edges.length;
    const walk = new Int32Array(n).fill(-1); // id of the walk that first visited the node
    const dist = new Int32Array(n);          // step index within that walk
    let ans = -1;

    for (let s = 0; s < n; s++) {
        if (walk[s] !== -1) continue;
        let cur = s, step = 0;
        while (cur !== -1 && walk[cur] === -1) {
            walk[cur] = s;
            dist[cur] = step++;
            cur = edges[cur];
        }
        if (cur !== -1 && walk[cur] === s) {
            const len = step - dist[cur];
            if (len > ans) ans = len;
        }
    }
    return ans;
};
