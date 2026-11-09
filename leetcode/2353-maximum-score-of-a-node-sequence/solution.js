
var maximumScore = function(scores, edges) {
    const n = scores.length;

    // Store the top 3 neighbors of every node
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Sort neighbors by their scores in descending order
    for (let i = 0; i < n; i++) {
        graph[i].sort((a, b) => scores[b] - scores[a]);

        // Only the top 3 neighbors are needed
        graph[i] = graph[i].slice(0, 3);
    }

    let answer = -1;

    // Consider every edge as the middle edge
    for (const [b, c] of edges) {

        // Choose a neighbor of b
        for (const a of graph[b]) {

            // Choose a neighbor of c
            for (const d of graph[c]) {

                // All four nodes must be distinct
                if (
                    a === c ||
                    d === b ||
                    a === d
                ) {
                    continue;
                }

                const total =
                    scores[a] +
                    scores[b] +
                    scores[c] +
                    scores[d];

                answer = Math.max(answer, total);
            }
        }
    }

    return answer;
};

