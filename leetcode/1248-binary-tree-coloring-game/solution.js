var btreeGameWinningMove = function(root, n, x) {
    let leftCount = 0;
    let rightCount = 0;
    
    function countNodes(node) {
        if (!node) return 0;
        
        const l = countNodes(node.left);
        const r = countNodes(node.right);
        
        if (node.val === x) {
            leftCount = l;
            rightCount = r;
        }
        
        return 1 + l + r;
    }
    
    countNodes(root);
    const parentCount = n - (1 + leftCount + rightCount);
    
    return Math.max(leftCount, rightCount, parentCount) > Math.floor(n / 2);
};
