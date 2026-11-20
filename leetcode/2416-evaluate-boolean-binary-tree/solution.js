var evaluateTree = function(root) {
    // Leaf node: 0 -> false, 1 -> true
    if (!root.left && !root.right) {
        return root.val === 1;
    }
    
    // Internal node: 2 -> OR, 3 -> AND (with short-circuiting)
    if (root.val === 2) {
        return evaluateTree(root.left) || evaluateTree(root.right);
    }
    
    return evaluateTree(root.left) && evaluateTree(root.right);
};
