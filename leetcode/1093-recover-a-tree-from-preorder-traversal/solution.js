var recoverFromPreorder = function(traversal) {
    const stack = [];
    let i = 0;
    const n = traversal.length;
    
    while (i < n) {
        // 1. Count dashes to determine depth
        let depth = 0;
        while (i < n && traversal[i] === '-') {
            depth++;
            i++;
        }
        
        // 2. Parse node value
        let val = 0;
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9') {
            val = val * 10 + (traversal.charCodeAt(i) - 48);
            i++;
        }
        
        const node = new TreeNode(val);
        
        // 3. Pop finished subtrees until stack top is the parent at (depth - 1)
        while (stack.length > depth) {
            stack.pop();
        }
        
        // 4. Attach to parent (left first, then right)
        if (stack.length > 0) {
            const parent = stack[stack.length - 1];
            if (!parent.left) {
                parent.left = node;
            } else {
                parent.right = node;
            }
        }
        
        stack.push(node);
    }
    
    return stack[0];
};
