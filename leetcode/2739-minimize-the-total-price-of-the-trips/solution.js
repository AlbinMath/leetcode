
var minimumTotalPrice = function(n, edges, price, trips) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Count visits to every node.
    const count = new Array(n).fill(0);

    function findPath(u, parent, target) {
        if (u === target) {
            count[u]++;
            return true;
        }

        for (const v of graph[u]) {
            if (v === parent) continue;

            if (findPath(v, u, target)) {
                count[u]++;
                return true;
            }
        }

        return false;
    }

    for (const [start, end] of trips) {
        findPath(start, -1, end);
    }

    // Step 2: Tree DP.
    // dp[u][0] = minimum cost when u is not halved.
    // dp[u][1] = minimum cost when u is halved.

    function dfs(u, parent) {
        let full = count[u] * price[u];
        let half = count[u] * (price[u] / 2);

        for (const v of graph[u]) {
            if (v === parent) continue;

            const [childFull, childHalf] = dfs(v, u);

            // If u is not halved, child can be either.
            full += Math.min(childFull, childHalf);

            // If u is halved, child cannot be halved.
            half += childFull;
        }

        return [full, half];
    }

    const [full, half] = dfs(0, -1);

    return Math.min(full, half);
};

