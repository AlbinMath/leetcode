
var criticalConnections = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);

    // Build adjacency list
    for (const [u, v] of connections) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const disc = new Array(n).fill(-1);
    const low = new Array(n).fill(-1);
    const bridges = [];

    let time = 0;

    function dfs(node, parent) {
        disc[node] = low[node] = time++;

        for (const neighbor of graph[node]) {
            if (neighbor === parent) continue;

            if (disc[neighbor] === -1) {
                // Visit an unvisited neighbor
                dfs(neighbor, node);

                // Update low-link value
                low[node] = Math.min(low[node], low[neighbor]);

                // Check whether this edge is a bridge
                if (low[neighbor] > disc[node]) {
                    bridges.push([node, neighbor]);
                }
            } else {
                // Back edge to an already visited node
                low[node] = Math.min(low[node], disc[neighbor]);
            }
        }
    }

    // Start DFS from node 0
    dfs(0, -1);

    return bridges;
};

