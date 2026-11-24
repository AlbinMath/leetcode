
var countPairs = function(n, edges, queries) {
    const degree = new Array(n + 1).fill(0);

    // Count edges between each pair of nodes
    const common = new Map();

    for (const [u, v] of edges) {
        degree[u]++;
        degree[v]++;

        const a = Math.min(u, v);
        const b = Math.max(u, v);

        const key = a * (n + 1) + b;

        common.set(key, (common.get(key) || 0) + 1);
    }

    // Sort node degrees
    const sorted = degree.slice(1).sort((a, b) => a - b);

    const answers = [];

    for (const query of queries) {
        let left = 0;
        let right = n - 1;
        let count = 0;

        // Count pairs using two pointers
        while (left < right) {
            if (sorted[left] + sorted[right] > query) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }

        // Correct pairs that were overcounted
        // because of multiple edges between two nodes
        for (const [key, shared] of common) {
            const a = Math.floor(key / (n + 1));
            const b = key % (n + 1);

            const sum = degree[a] + degree[b];

            if (sum > query && sum - shared <= query) {
                count--;
            }
        }

        answers.push(count);
    }

    return answers;
};

