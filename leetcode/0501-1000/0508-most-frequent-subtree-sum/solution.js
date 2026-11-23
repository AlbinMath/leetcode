
var findFrequentTreeSum = function(root) {
    const counts = new Map();
    let maxFreq = 0;
    
    function dfs(node) {
        if (!node) return 0;
        
        const currSum = node.val + dfs(node.left) + dfs(node.right);
        const freq = (counts.get(currSum) || 0) + 1;
        counts.set(currSum, freq);
        
        if (freq > maxFreq) {
            maxFreq = freq;
        }
        
        return currSum;
    }
    
    dfs(root);
    
    const result = [];
    for (const [sum, freq] of counts.entries()) {
        if (freq === maxFreq) {
            result.push(sum);
        }
    }
    
    return result;
};
