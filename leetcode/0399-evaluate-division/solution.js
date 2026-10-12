var calcEquation = function(equations, values, queries) {
    const graph = new Map();

    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const value = values[i];

        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);

        graph.get(a).push([b, value]);
        graph.get(b).push([a, 1 / value]);
    }

    function dfs(start, end, visited) {
        if (!graph.has(start) || !graph.has(end)) {
            return -1.0;
        }

        if (start === end) {
            return 1.0;
        }

        visited.add(start);

        for (const [neighbor, weight] of graph.get(start)) {
            if (!visited.has(neighbor)) {
                const result = dfs(neighbor, end, visited);

                if (result !== -1.0) {
                    return weight * result;
                }
            }
        }

        return -1.0;
    }

    return queries.map(([a, b]) => dfs(a, b, new Set()));
};
