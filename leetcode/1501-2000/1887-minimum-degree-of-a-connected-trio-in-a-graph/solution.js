
var minTrioDegree = function(n, edges) {
    // Build adjacency matrix
    const graph = Array.from(
        { length: n + 1 },
        () => new Array(n + 1).fill(false)
    );

    // Count edges connected to each node
    const degree = new Array(n + 1).fill(0);

    for (const [u, v] of edges) {
        graph[u][v] = true;
        graph[v][u] = true;

        degree[u]++;
        degree[v]++;
    }

    let minDegree = Infinity;

    // Check every possible trio
    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {

            // First two nodes must be connected
            if (!graph[i][j]) continue;

            for (let k = j + 1; k <= n; k++) {

                // All three pairs must be connected
                if (graph[i][k] && graph[j][k]) {

                    // Remove the three internal edges
                    const trioDegree =
                        degree[i] + degree[j] + degree[k] - 6;

                    minDegree = Math.min(
                        minDegree,
                        trioDegree
                    );
                }
            }
        }
    }

    return minDegree === Infinity ? -1 : minDegree;
};

