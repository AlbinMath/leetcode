
var baseUnitConversions = function(conversions) {
    const MOD = 1000000007n;
    const n = conversions.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [source, target, factor] of conversions) {
        graph[source].push([target, BigInt(factor)]);
    }

    const ans = new Array(n).fill(0n);
    ans[0] = 1n;

    const queue = [0];
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];

        for (const [v, factor] of graph[u]) {
            ans[v] = (ans[u] * factor) % MOD;
            queue.push(v);
        }
    }

    // Convert BigInt results back to Numbers for LeetCode.
    return ans.map(value => Number(value));
};

