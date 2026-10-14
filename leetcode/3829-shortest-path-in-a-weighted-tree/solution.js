
var treeQueries = function(n, edges, queries) {
    const adj = Array.from({ length: n + 1 }, () => []);
    const edgeMap = new Map();

    for (let i = 0; i < edges.length; i++) {
        const [u, v, w] = edges[i];

        adj[u].push([v, w, i]);
        adj[v].push([u, w, i]);

        const key = `${Math.min(u, v)},${Math.max(u, v)}`;
        edgeMap.set(key, i);
    }

    const tin = new Array(n + 1).fill(0);
    const tout = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    const edgeChild = new Array(n - 1).fill(0);
    const edgeWeight = edges.map(e => e[2]);

    // Iterative DFS: safe for a tree of depth 100000.
    let timer = 0;
    const stack = [[1, 0, 0]];

    while (stack.length) {
        const [u, p, state] = stack.pop();

        if (state === 0) {
            tin[u] = timer++;
            stack.push([u, p, 1]);

            for (let i = adj[u].length - 1; i >= 0; i--) {
                const [v, w, id] = adj[u][i];

                if (v === p) continue;

                dist[v] = dist[u] + w;
                edgeChild[id] = v;
                stack.push([v, u, 0]);
            }
        } else {
            tout[u] = timer - 1;
        }
    }

    // Fenwick tree for subtree range additions.
    const bit = new Array(n + 2).fill(0);

    function add(index, delta) {
        for (let i = index + 1; i <= n + 1; i += i & -i) {
            bit[i] += delta;
        }
    }

    function prefix(index) {
        let sum = 0;

        for (let i = index + 1; i > 0; i -= i & -i) {
            sum += bit[i];
        }

        return sum;
    }

    const answer = [];

    for (const query of queries) {
        if (query[0] === 1) {
            const [, u, v, newWeight] = query;
            const key = `${Math.min(u, v)},${Math.max(u, v)}`;
            const id = edgeMap.get(key);

            const delta = newWeight - edgeWeight[id];
            edgeWeight[id] = newWeight;

            const child = edgeChild[id];

            // Update all root distances in this child's subtree.
            add(tin[child], delta);
            add(tout[child] + 1, -delta);
        } else {
            const x = query[1];
            answer.push(dist[x] + prefix(tin[x]));
        }
    }

    return answer;
};

