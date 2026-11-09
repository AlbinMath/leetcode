
var maxStarSum = function(vals, edges, k) {
    const n = vals.length;

    const graph = Array.from({ length: n }, () => []);

    // Build undirected graph.
    for (const [u, v] of edges) {
        graph[u].push(vals[v]);
        graph[v].push(vals[u]);
    }

    let answer = -Infinity;

    // Try every node as the center.
    for (let i = 0; i < n; i++) {
        // Keep only positive neighbor values.
        const neighbors = graph[i].filter(value => value > 0);

        // Sort in descending order.
        neighbors.sort((a, b) => b - a);

        // Start with the center's own value.
        let sum = vals[i];

        // Add at most k highest positive neighbors.
        for (let j = 0; j < Math.min(k, neighbors.length); j++) {
            sum += neighbors[j];
        }

        answer = Math.max(answer, sum);
    }

    return answer;
};

