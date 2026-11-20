var countDominantNodes = function(root) {
    let dominantCount = 0;
    
    function dfs(node) {
        if (!node) return 0;
        
        const leftMax = dfs(node.left);
        const rightMax = dfs(node.right);
        
        const currMax = Math.max(node.val, leftMax, rightMax);
        if (currMax === node.val) {
            dominantCount++;
        }
        
        return currMax;
    }
    
    dfs(root);
    return dominantCount;
};
