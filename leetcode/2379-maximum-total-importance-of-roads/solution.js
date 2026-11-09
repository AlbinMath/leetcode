
var maximumImportance = function(n, roads) {
    // Count the number of roads connected to each city
    const degree = new Array(n).fill(0);

    for (const [u, v] of roads) {
        degree[u]++;
        degree[v]++;
    }

    // Sort cities by degree in ascending order
    degree.sort((a, b) => a - b);

    let total = 0;

    // Assign values from 1 to n
    for (let i = 0; i < n; i++) {
        total += degree[i] * (i + 1);
    }

    return total;
};

