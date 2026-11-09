
var frogPosition = function(n, edges, t, target) {
    // Build adjacency list
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    function dfs(node, parent, time, probability) {
        // Reached the target at the required time
        if (time === t) {
            return node === target ? probability : 0;
        }

        // Count unvisited neighbors
        let children = 0;

        for (const neighbor of graph[node]) {
            if (neighbor !== parent) {
                children++;
            }
        }

        // Frog cannot move, so it stays here
        if (children === 0) {
            return node === target ? probability : 0;
        }

        // Try every unvisited neighbor
        for (const neighbor of graph[node]) {
            if (neighbor !== parent) {
                const result = dfs(
                    neighbor,
                    node,
                    time + 1,
                    probability / children
                );

                if (result > 0) {
                    return result;
                }
            }
        }

        return 0;
    }

    return dfs(1, 0, 0, 1);
};

