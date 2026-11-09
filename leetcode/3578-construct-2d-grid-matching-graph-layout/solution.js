
var constructGridLayout = function(n, edges) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const degree = graph.map(g => g.length);

    // Case 1: Single row or single column (a path).
    const endpoint = degree.indexOf(1);

    if (endpoint !== -1) {
        const result = [];
        let prev = -1;
        let curr = endpoint;

        while (curr !== -1) {
            result.push(curr);

            let next = -1;

            for (const v of graph[curr]) {
                if (v !== prev) {
                    next = v;
                    break;
                }
            }

            prev = curr;
            curr = next;
        }

        return [result];
    }

    // Case 2: Two-dimensional grid.
    // Start from any corner (degree 2).
    const corner = degree.indexOf(2);

    const firstRow = [corner];

    let prev = -1;
    let curr = corner;

    // Choose the neighbor with the smaller degree.
    // If both have equal degree, either direction works.
    let next = graph[curr][0];

    for (const v of graph[curr]) {
        if (degree[v] < degree[next]) {
            next = v;
        }
    }

    firstRow.push(next);

    prev = curr;
    curr = next;

    // Continue along the first row until reaching another corner.
    while (degree[curr] !== 2) {
        let nextNode = -1;

        for (const v of graph[curr]) {
            if (v === prev) continue;

            if (
                nextNode === -1 ||
                degree[v] < degree[nextNode]
            ) {
                nextNode = v;
            }
        }

        if (nextNode === -1) break;

        firstRow.push(nextNode);

        prev = curr;
        curr = nextNode;
    }

    // Mark all nodes in the first row.
    const used = new Uint8Array(n);

    for (const v of firstRow) {
        used[v] = 1;
    }

    const result = [firstRow];
    let currentRow = firstRow;

    // Build remaining rows.
    while (currentRow.length > 0) {
        const nextRow = [];

        for (const u of currentRow) {
            for (const v of graph[u]) {
                if (!used[v]) {
                    used[v] = 1;
                    nextRow.push(v);
                    break;
                }
            }
        }

        if (nextRow.length === 0) break;

        result.push(nextRow);
        currentRow = nextRow;
    }

    return result;
};

