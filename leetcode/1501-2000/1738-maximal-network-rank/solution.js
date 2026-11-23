
var maximalNetworkRank = function(n, roads) {
    // Count the number of roads connected to each city
    const degree = new Array(n).fill(0);

    // Track whether two cities are directly connected
    const connected = Array.from(
        { length: n },
        () => new Array(n).fill(false)
    );

    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;

        connected[a][b] = true;
        connected[b][a] = true;
    }

    let maxRank = 0;

    // Check every pair of different cities
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let rank = degree[i] + degree[j];

            // Count the shared road only once
            if (connected[i][j]) {
                rank--;
            }

            maxRank = Math.max(maxRank, rank);
        }
    }

    return maxRank;
};

