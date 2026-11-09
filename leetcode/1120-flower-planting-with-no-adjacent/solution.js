
var gardenNoAdj = function(n, paths) {
    // Build adjacency list
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [u, v] of paths) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Store flower type for each garden
    const answer = new Array(n + 1).fill(0);

    // Assign flowers greedily
    for (let garden = 1; garden <= n; garden++) {
        const used = new Set();

        // Collect flower types of neighboring gardens
        for (const neighbor of graph[garden]) {
            if (answer[neighbor] !== 0) {
                used.add(answer[neighbor]);
            }
        }

        // Choose the first available flower type
        for (let flower = 1; flower <= 4; flower++) {
            if (!used.has(flower)) {
                answer[garden] = flower;
                break;
            }
        }
    }

    return answer.slice(1);
};

