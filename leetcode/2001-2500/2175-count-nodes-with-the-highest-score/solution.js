var countHighestScoreNodes = function(parents) {
    const n = parents.length;
    const children = Array.from({ length: n }, () => []);
    
    for (let i = 1; i < n; i++) {
        children[parents[i]].push(i);
    }
    
    let maxScore = 0;
    let count = 0;
    
    function dfs(node) {
        let score = 1;
        let subtreeSize = 1;
        
        // Multiply sizes of existing child subtrees
        for (const child of children[node]) {
            const childSize = dfs(child);
            score *= childSize;
            subtreeSize += childSize;
        }
        
        // Multiply size of the remaining upper component (if non-empty)
        const remaining = n - subtreeSize;
        if (remaining > 0) {
            score *= remaining;
        }
        
        if (score > maxScore) {
            maxScore = score;
            count = 1;
        } else if (score === maxScore) {
            count++;
        }
        
        return subtreeSize;
    }
    
    dfs(0);
    return count;
};
