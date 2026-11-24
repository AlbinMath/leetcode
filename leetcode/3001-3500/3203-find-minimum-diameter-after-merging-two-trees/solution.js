
var minimumDiameterAfterMerge = function(edges1, edges2) {

    function findDiameter(edges) {
        const n = edges.length + 1;

        const graph = Array.from({ length: n }, () => []);

        for (const [u, v] of edges) {
            graph[u].push(v);
            graph[v].push(u);
        }

        // BFS to find the farthest node.
        function bfs(start) {
            const dist = new Array(n).fill(-1);
            const queue = [start];

            dist[start] = 0;
            let head = 0;
            let farthest = start;

            while (head < queue.length) {
                const u = queue[head++];

                if (dist[u] > dist[farthest]) {
                    farthest = u;
                }

                for (const v of graph[u]) {
                    if (dist[v] === -1) {
                        dist[v] = dist[u] + 1;
                        queue.push(v);
                    }
                }
            }

            return [farthest, dist[farthest]];
        }

        // First BFS: find one endpoint of the diameter.
        const [endpoint] = bfs(0);

        // Second BFS: find the diameter.
        const [, diameter] = bfs(endpoint);

        return diameter;
    }

    const d1 = findDiameter(edges1);
    const d2 = findDiameter(edges2);

    const radius1 = Math.ceil(d1 / 2);
    const radius2 = Math.ceil(d2 / 2);

    return Math.max(
        d1,
        d2,
        radius1 + radius2 + 1
    );
};

