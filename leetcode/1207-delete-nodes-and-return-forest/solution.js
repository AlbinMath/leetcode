var delNodes = function(root, to_delete) {
    const deleteSet = new Set(to_delete);
    const forest = [];
    
    function dfs(node, isRoot) {
        if (!node) return null;
        
        const deleted = deleteSet.has(node.val);
        
        // If this node survives and has no parent, it is a root in the forest
        if (!deleted && isRoot) {
            forest.push(node);
        }
        
        // If current node is deleted, its children become new roots
        node.left = dfs(node.left, deleted);
        node.right = dfs(node.right, deleted);
        
        return deleted ? null : node;
    }
    
    dfs(root, true);
    return forest;
};
