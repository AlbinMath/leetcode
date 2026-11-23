var removeLeafNodes = function(root, target) {
    if (!root) return null;
    
    // Prune children first (post-order)
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    
    // If current node is now a leaf with value === target, delete it
    if (!root.left && !root.right && root.val === target) {
        return null;
    }
    
    return root;
};
