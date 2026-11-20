var minIncrements = function(n, cost) {
    let increments = 0;
    
    // Traverse all non-leaf nodes bottom-up
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        const left = 2 * i + 1;
        const right = 2 * i + 2;
        
        // Equalize the left and right subtree path sums
        increments += Math.abs(cost[left] - cost[right]);
        
        // Propagate the max equalized subtree path sum upward
        cost[i] += Math.max(cost[left], cost[right]);
    }
    
    return increments;
};
