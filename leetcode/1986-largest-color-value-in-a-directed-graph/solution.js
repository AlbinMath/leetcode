/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function (colors, edges) {
    const n = colors.length;
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    for (const [a, b] of edges) {
        adj[a].push(b);
        indeg[b]++;
    }

    const dp = new Int32Array(n * 26);
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let head = 0, ans = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const cu = colors.charCodeAt(u) - 97;
        const val = ++dp[u * 26 + cu];
        if (val > ans) ans = val;

        for (const v of adj[u]) {
            const bu = u * 26, bv = v * 26;
            for (let c = 0; c < 26; c++) {
                if (dp[bu + c] > dp[bv + c]) dp[bv + c] = dp[bu + c];
            }
            if (--indeg[v] === 0) queue.push(v);
        }
    }
    return head === n ? ans : -1;
};
