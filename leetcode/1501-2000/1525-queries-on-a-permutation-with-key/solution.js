
var processQueries = function(queries, m) {
    const permutation = Array.from(
        { length: m },
        (_, i) => i + 1
    );

    const result = [];

    for (const query of queries) {
        // Find the current index of the query
        const index = permutation.indexOf(query);

        result.push(index);

        // Remove the element from its current position
        permutation.splice(index, 1);

        // Move it to the beginning
        permutation.unshift(query);
    }

    return result;
};

