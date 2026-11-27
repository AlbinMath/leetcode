
var placedCoins = function(edges, cost) {
    const n = cost.length;

    const adj = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const parent = new Array(n).fill(-1);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const node = order[i];

        for (const child of adj[node]) {
            if (child === parent[node]) continue;

            parent[child] = node;
            order.push(child);
        }
    }

    const size = new Array(n).fill(1);
    const extremes = Array.from({ length: n }, () => []);
    const coins = new Array(n).fill(1);

    for (let i = n - 1; i >= 0; i--) {
        const node = order[i];

        const values = [cost[node]];

        for (const child of adj[node]) {
            if (parent[child] !== node) continue;

            size[node] += size[child];
            values.push(...extremes[child]);
        }

        values.sort((a, b) => a - b);

        if (values.length > 5) {
            extremes[node] = [
                values[0],
                values[1],
                ...values.slice(-3)
            ];
        } else {
            extremes[node] = values;
        }

        if (size[node] < 3) {
            coins[node] = 1;
            continue;
        }

        const len = extremes[node].length;

        const product1 =
            extremes[node][len - 1] *
            extremes[node][len - 2] *
            extremes[node][len - 3];

        const product2 =
            extremes[node][0] *
            extremes[node][1] *
            extremes[node][len - 1];

        coins[node] = Math.max(0, product1, product2);
    }

    return coins;
};

