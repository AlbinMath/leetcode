
var findChampion = function(n, edges) {
    const indegree = new Array(n).fill(0);

    // Count incoming edges for each team.
    for (const [u, v] of edges) {
        indegree[v]++;
    }

    let champion = -1;

    // Find the unique team with indegree 0.
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            if (champion !== -1) {
                return -1;
            }

            champion = i;
        }
    }

    return champion;
};

