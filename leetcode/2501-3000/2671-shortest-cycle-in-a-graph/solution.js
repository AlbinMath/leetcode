
var findShortestCycle = function(n, edges) {
    const graph = Array.from({ length: n }, () => []);

    // Build undirected graph.
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    let answer = Infinity;

    // BFS from every node.
    for (let start = 0; start < n; start++) {
        const dist = new Array(n).fill(-1);
        const parent = new Array(n).fill(-1);

        const queue = [start];
        let head = 0;

        dist[start] = 0;

        while (head < queue.length) {
            const u = queue[head++];

            // No cycle shorter than this can improve the answer.
            if (2 * dist[u] + 1 >= answer) {
                continue;
            }

            for (const v of graph[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    queue.push(v);
                } 
                else if (parent[u] !== v) {
                    const cycleLength = dist[u] + dist[v] + 1;
                    answer = Math.min(answer, cycleLength);
                }
            }
        }
    }

    return answer === Infinity ? -1 : answer;
};

