var kthLargestPerfectSubtree = function(root, k) {
    const sizes = [];
    
    function dfs(node) {
        if (!node) return 0;
        
        const leftSize = dfs(node.left);
        const rightSize = dfs(node.right);
        
        // Valid perfect subtree if both children are valid and have equal sizes
        if (leftSize !== -1 && leftSize === rightSize) {
            const currSize = leftSize + rightSize + 1;
            sizes.push(currSize);
            return currSize;
        }
        
        return -1;
    }
    
    dfs(root);
    
    if (sizes.length < k) {
        return -1;
    }
    
    sizes.sort((a, b) => b - a);
    return sizes[k - 1];
};
