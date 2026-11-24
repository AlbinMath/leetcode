
var minimumThreshold = function(n, edges, source, target, k) {
    if (source === target) return 0;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);
    let maxWeight = 0;

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);

        maxWeight = Math.max(maxWeight, w);
    }

    // Check if target can be reached using at most k heavy edges
    function canReach(threshold) {
        const dist = new Array(n).fill(Infinity);
        const visited = new Array(n).fill(false);

        dist[source] = 0;

        // Dijkstra: minimize the number of heavy edges
        for (let i = 0; i < n; i++) {
            let u = -1;

            for (let j = 0; j < n; j++) {
                if (
                    !visited[j] &&
                    (u === -1 || dist[j] < dist[u])
                ) {
                    u = j;
                }
            }

            if (u === -1 || dist[u] === Infinity) {
                break;
            }

            if (u === target) {
                return dist[u] <= k;
            }

            visited[u] = true;

            for (const [v, w] of graph[u]) {
                if (visited[v]) continue;

                const cost = w > threshold ? 1 : 0;
                const newDist = dist[u] + cost;

                if (newDist < dist[v]) {
                    dist[v] = newDist;
                }
            }
        }

        return dist[target] <= k;
    }

    // Check whether a path exists at the maximum threshold
    if (!canReach(maxWeight)) {
        return -1;
    }

    // Binary search from 0 to maximum edge weight
    let left = 0;
    let right = maxWeight;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (canReach(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
};

