var minReorder = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);

    for (const [a, b] of connections) {
        graph[a].push([b, 1]);
        graph[b].push([a, 0]);
    }

    const visited = new Array(n).fill(false);
    let changes = 0;

    function dfs(city) {
        visited[city] = true;

        for (const [neighbor, cost] of graph[city]) {
            if (!visited[neighbor]) {
                changes += cost;
                dfs(neighbor);
            }
        }
    }

    dfs(0);

    return changes;
};
