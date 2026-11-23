
var checkWays = function(pairs) {
    // Build the graph
    const graph = new Map();

    for (const [x, y] of pairs) {
        if (!graph.has(x)) graph.set(x, new Set());
        if (!graph.has(y)) graph.set(y, new Set());

        graph.get(x).add(y);
        graph.get(y).add(x);
    }

    const nodes = [...graph.keys()];
    const n = nodes.length;

    // Find a possible root:
    // The root must be connected to all other nodes.
    let root = -1;

    for (const node of nodes) {
        if (graph.get(node).size === n - 1) {
            root = node;
            break;
        }
    }

    // No possible root
    if (root === -1) return 0;

    let result = 1;

    // Process every node except the root
    for (const node of nodes) {
        if (node === root) continue;

        const neighbors = graph.get(node);
        const degree = neighbors.size;

        let parent = -1;
        let parentDegree = Infinity;

        // Find the neighbor with the smallest degree
        // that is greater than or equal to this node's degree.
        for (const neighbor of neighbors) {
            const neighborDegree = graph.get(neighbor).size;

            if (
                neighborDegree >= degree &&
                neighborDegree < parentDegree
            ) {
                parent = neighbor;
                parentDegree = neighborDegree;
            }
        }

        // Every non-root node must have a parent
        if (parent === -1) return 0;

        // All neighbors of this node must also be
        // neighbors of its parent.
        for (const neighbor of neighbors) {
            if (
                neighbor !== parent &&
                !graph.get(parent).has(neighbor)
            ) {
                return 0;
            }
        }

        // Equal degrees mean multiple valid parent choices
        if (parentDegree === degree) {
            result = 2;
        }
    }

    return result;
};

