var sufficientSubset = function(root, limit) {
    if (!root) return null;
    
    // Original leaf: check if path sum meets the limit
    if (!root.left && !root.right) {
        return root.val < limit ? null : root;
    }
    
    // Recursively prune children with remaining required sum
    root.left = sufficientSubset(root.left, limit - root.val);
    root.right = sufficientSubset(root.right, limit - root.val);
    
    // If both subtrees were completely pruned, no valid path passes through root
    if (!root.left && !root.right) {
        return null;
    }
    
    return root;
};
