
var mostProfitablePath = function(edges, bob, amount) {
    const n = amount.length;

    // Build undirected graph.
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Find parent and depth of every node.
    const parent = new Array(n).fill(-1);
    const depth = new Array(n).fill(0);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            depth[v] = depth[u] + 1;
            order.push(v);
        }
    }

    // Step 2: Calculate Bob's arrival time.
    const bobTime = new Array(n).fill(Infinity);

    let node = bob;
    let time = 0;

    while (node !== -2) {
        bobTime[node] = time++;
        node = parent[node];
    }

    // Step 3: DFS all Alice paths.
    let answer = -Infinity;

    const stack = [[0, -1, 0, 0]];
    // [node, parent, Alice time, current income]

    while (stack.length > 0) {
        const [u, p, aliceTime, income] = stack.pop();

        let gain = 0;

        if (aliceTime < bobTime[u]) {
            gain = amount[u];
        } else if (aliceTime === bobTime[u]) {
            gain = amount[u] / 2;
        }

        const currentIncome = income + gain;

        // A leaf is a node with no children.
        if (u !== 0 && graph[u].length === 1) {
            answer = Math.max(answer, currentIncome);
            continue;
        }

        for (const v of graph[u]) {
            if (v === p) continue;

            stack.push([
                v,
                u,
                aliceTime + 1,
                currentIncome
            ]);
        }
    }

    return answer;
};

