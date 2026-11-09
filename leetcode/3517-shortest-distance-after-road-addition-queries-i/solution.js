
var shortestDistanceAfterQueries = function(n, queries) {
    const graph = Array.from({ length: n }, () => []);

    // Add the original roads.
    for (let i = 0; i < n - 1; i++) {
        graph[i].push(i + 1);
    }

    const answer = [];

    for (const [u, v] of queries) {
        // Add the new directed road.
        graph[u].push(v);

        // BFS to find shortest distance from 0 to n - 1.
        const dist = new Array(n).fill(-1);
        const queue = [0];

        dist[0] = 0;
        let head = 0;

        while (head < queue.length) {
            const curr = queue[head++];

            if (curr === n - 1) break;

            for (const next of graph[curr]) {
                if (dist[next] === -1) {
                    dist[next] = dist[curr] + 1;
                    queue.push(next);
                }
            }
        }

        answer.push(dist[n - 1]);
    }

    return answer;
};

