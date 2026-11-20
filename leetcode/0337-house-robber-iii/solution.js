
var rob = function(root) {
    function dfs(node) {
        if (!node) return [0, 0];
        
        const [leftRob, leftSkip] = dfs(node.left);
        const [rightRob, rightSkip] = dfs(node.right);
        
        const robCurr = node.val + leftSkip + rightSkip;
        const skipCurr = Math.max(leftRob, leftSkip) + Math.max(rightRob, rightSkip);
        
        return [robCurr, skipCurr];
    }
    
    return Math.max(...dfs(root));
};
