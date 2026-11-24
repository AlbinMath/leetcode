var countPairs = function(root, distance) {
    let goodPairs = 0;
    
    function dfs(node) {
        const counts = new Array(distance + 1).fill(0);
        if (!node) return counts;
        
        // Leaf node is at distance 1 from its parent
        if (!node.left && !node.right) {
            counts[1] = 1;
            return counts;
        }
        
        const leftCounts = dfs(node.left);
        const rightCounts = dfs(node.right);
        
        // Count pairs whose LCA is the current node
        for (let l = 1; l <= distance; l++) {
            if (leftCounts[l] === 0) continue;
            for (let r = 1; r <= distance - l; r++) {
                goodPairs += leftCounts[l] * rightCounts[r];
            }
        }
        
        // Shift distances up by 1 for the parent node
        for (let d = 1; d < distance; d++) {
            counts[d + 1] = leftCounts[d] + rightCounts[d];
        }
        
        return counts;
    }
    
    dfs(root);
    return goodPairs;
};
