
var maxScore = function(n, edges) {
    const sumOfSquares = n * (n + 1) * (2 * n + 1) / 6;

    if (edges.length === n) {
        // Cycle
        return sumOfSquares - (2 * n - 3);
    }

    // Path
    return sumOfSquares - (2 * n - 1);
};

