
var validArrangement = function(pairs) {
    const graph = new Map();
    const inDegree = new Map();
    const outDegree = new Map();

    // Build directed graph and calculate degrees
    for (const [u, v] of pairs) {
        if (!graph.has(u)) graph.set(u, []);

        graph.get(u).push(v);

        outDegree.set(u, (outDegree.get(u) || 0) + 1);
        inDegree.set(v, (inDegree.get(v) || 0) + 1);

        // Ensure both nodes exist in degree maps
        if (!inDegree.has(u)) inDegree.set(u, 0);
        if (!outDegree.has(v)) outDegree.set(v, 0);
    }

    // Find Eulerian path starting node
    let start = pairs[0][0];

    for (const node of graph.keys()) {
        const out = outDegree.get(node) || 0;
        const incoming = inDegree.get(node) || 0;

        if (out - incoming === 1) {
            start = node;
            break;
        }
    }

    // Hierholzer's algorithm (iterative DFS)
    const stack = [start];
    const path = [];

    while (stack.length > 0) {
        const node = stack[stack.length - 1];
        const neighbors = graph.get(node);

        if (neighbors && neighbors.length > 0) {
            stack.push(neighbors.pop());
        } else {
            path.push(stack.pop());
        }
    }

    // Reverse the Eulerian path
    path.reverse();

    // Convert node sequence into pairs
    const result = [];

    for (let i = 0; i < path.length - 1; i++) {
        result.push([path[i], path[i + 1]]);
    }

    return result;
};

