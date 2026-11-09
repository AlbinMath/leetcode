
var timeTaken = function(edges) {
    const n = edges.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const cost = (node) => node % 2 === 0 ? 2 : 1;

    const parent = new Array(n).fill(-1);
    const order = [0];

    // First traversal: establish parent-child relationships.
    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            order.push(v);
        }
    }

    // down[u]: maximum time from u to a node in its subtree.
    const down = new Array(n).fill(0);

    // Process nodes in reverse order (children before parents).
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];

        for (const v of graph[u]) {
            if (parent[v] === u) {
                down[u] = Math.max(
                    down[u],
                    cost(v) + down[v]
                );
            }
        }
    }

    // up[u]: maximum time from u to a node outside its subtree.
    const up = new Array(n).fill(0);

    const answer = new Array(n);

    // Process parents before children.
    for (const u of order) {
        let best1 = 0;
        let best2 = 0;
        let bestChild = -1;

        // Find the two largest child contributions.
        for (const v of graph[u]) {
            if (parent[v] !== u) continue;

            const value = cost(v) + down[v];

            if (value > best1) {
                best2 = best1;
                best1 = value;
                bestChild = v;
            } else if (value > best2) {
                best2 = value;
            }
        }

        answer[u] = Math.max(down[u], up[u]);

        // Calculate up values for each child.
        for (const v of graph[u]) {
            if (parent[v] !== u) continue;

            // Best path from u that does not enter v's subtree.
            const bestOther = (v === bestChild) ? best2 : best1;

            up[v] = cost(u) + Math.max(up[u], bestOther);
        }
    }

    return answer;
};

