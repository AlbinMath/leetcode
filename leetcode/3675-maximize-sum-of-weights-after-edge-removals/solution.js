
var maximizeSumOfWeights = function(edges, k) {
    const n = edges.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    const parent = new Array(n).fill(-1);
    const parentWeight = new Array(n).fill(0);

    const order = [0];
    parent[0] = 0;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const [v, w] of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            parentWeight[v] = w;

            order.push(v);
        }
    }

    const dp0 = new Array(n).fill(0);
    const dp1 = new Array(n).fill(0);

    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];

        let base = 0;
        const gains = [];

        for (const [v, w] of graph[u]) {
            if (parent[v] !== u) continue;

            base += dp0[v];

            const gain = w + dp1[v] - dp0[v];

            if (gain > 0) {
                gains.push(gain);
            }
        }

        gains.sort((a, b) => b - a);

        dp0[u] = base;

        for (let j = 0; j < Math.min(k, gains.length); j++) {
            dp0[u] += gains[j];
        }

        dp1[u] = base;

        for (let j = 0; j < Math.min(k - 1, gains.length); j++) {
            dp1[u] += gains[j];
        }
    }

    return dp0[0];
};

