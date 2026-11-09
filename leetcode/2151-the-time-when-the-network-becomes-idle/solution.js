
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // BFS to calculate shortest distance from server 0
    const dist = new Array(n).fill(-1);
    const queue = [0];

    dist[0] = 0;

    let index = 0;

    while (index < queue.length) {
        const node = queue[index++];

        for (const neighbor of graph[node]) {
            if (dist[neighbor] === -1) {
                dist[neighbor] = dist[node] + 1;
                queue.push(neighbor);
            }
        }
    }

    let lastMessageTime = 0;

    // Calculate the last reply arrival time
    for (let i = 1; i < n; i++) {
        const roundTrip = dist[i] * 2;

        // Time when the last repeated message was sent
        const lastSend = Math.floor(
            (roundTrip - 1) / patience[i]
        ) * patience[i];

        // Last reply arrival time
        const lastReply = lastSend + roundTrip;

        lastMessageTime = Math.max(
            lastMessageTime,
            lastReply
        );
    }

    // Network becomes idle one second after the last reply
    return lastMessageTime + 1;
};

