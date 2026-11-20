var pathInZigZagTree = function(label) {
    let depth = Math.floor(Math.log2(label));
    const path = [];
    
    while (label >= 1) {
        path.push(label);
        const levelMin = 1 << depth;
        const levelMax = (1 << (depth + 1)) - 1;
        
        // Mirror current label across its row, then divide by 2 for its parent
        label = Math.floor((levelMin + levelMax - label) / 2);
        depth--;
    }
    
    return path.reverse();
};
