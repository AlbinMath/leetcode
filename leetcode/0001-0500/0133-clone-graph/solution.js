
var cloneGraph = function(node) {
    if (node === null) return null;

    const clones = new Map();

    function dfs(original) {
        // Return the clone if this node was already visited
        if (clones.has(original)) {
            return clones.get(original);
        }

        // Create a copy of the current node
        const copy = new Node(original.val, []);

        // Store it before exploring neighbors to handle cycles
        clones.set(original, copy);

        // Clone and connect all neighbors
        for (const neighbor of original.neighbors) {
            copy.neighbors.push(dfs(neighbor));
        }

        return copy;
    }

    return dfs(node);
};

