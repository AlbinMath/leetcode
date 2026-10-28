/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var getAncestors = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) adj[a].push(b);

    const ans = Array.from({ length: n }, () => []);
    const seen = new Int32Array(n).fill(-1);

    for (let u = 0; u < n; u++) {
        const stack = [u];
        seen[u] = u;
        while (stack.length) {
            const x = stack.pop();
            for (const y of adj[x]) {
                if (seen[y] !== u) {
                    seen[y] = u;
                    ans[y].push(u);
                    stack.push(y);
                }
            }
        }
    }
    return ans;
};
