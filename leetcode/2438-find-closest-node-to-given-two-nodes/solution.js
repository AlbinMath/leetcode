
var closestMeetingNode = function(edges, node1, node2) {
    const n = edges.length;

    // Calculate distances from a starting node
    function getDistances(start) {
        const dist = new Array(n).fill(-1);

        let current = start;
        let distance = 0;

        while (current !== -1 && dist[current] === -1) {
            dist[current] = distance++;

            current = edges[current];
        }

        return dist;
    }

    // Distances from both starting nodes
    const dist1 = getDistances(node1);
    const dist2 = getDistances(node2);

    let answer = -1;
    let minMaxDistance = Infinity;

    // Find the best common reachable node
    for (let i = 0; i < n; i++) {
        if (dist1[i] !== -1 && dist2[i] !== -1) {
            const maxDistance = Math.max(dist1[i], dist2[i]);

            if (maxDistance < minMaxDistance) {
                minMaxDistance = maxDistance;
                answer = i;
            }
        }
    }

    return answer;
};

